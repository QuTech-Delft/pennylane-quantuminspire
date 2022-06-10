# PennyLane-Quantum Inspire Plugin
#
# Copyright 2022 QuTech Delft
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module contains the :class:`~.QuantumInspireDevice` class, a PennyLane device that allows
evaluation and differentiation of Quantum Inspire's Quantum Processing Units (QPUs) using PennyLane.
"""

from abc import ABC
from time import localtime, strftime
from typing import Any, Dict, Iterable, Set, Union, Optional

from pennylane import DeviceError
from pennylane.wires import Wires
from pennylane_qiskit.qiskit_device import QiskitDevice

from qiskit.providers.backend import BackendV1 as Backend

from quantuminspire.credentials import load_account, get_token_authentication
from quantuminspire.qiskit import QI

from ._version import __version__


class QuantumInspireDevice(QiskitDevice, ABC):  # type: ignore
    """A PennyLane device for the QuantumInspire API (remote) backend.

    For more details, see the `Quantum Inspire documentation <https://github.com/QuTech-Delft/quantuminspire>`_

    You need to register at `Quantum Inspire <https://www.quantum-inspire.com/>`_ in order to
    receive a token that is used for authentication using the API.

    Args:
        wires (int or Iterable[Number, str]): Number of subsystems represented by the device,
            or iterable that contains unique labels for the subsystems as numbers (i.e., ``[-1, 0, 2]``)
            or strings (``['ancilla', 'q1', 'q2']``). Note that for some backends, the number
            of wires has to match the number of qubits accessible.

            The supported number of qubits for the Quantum Inspire backends are:
            'QX single-node simulator': between 1 and 26.
            'QX-34-L': between 1 and 34.
            'Spin-2': fixed number of 2.
            'Starmon-5': fixed number of 5.
        backend (str): the desired backend. Can be one of:
            'QX single-node simulator': A QuantumInspire QX single-node emulator backend.
            'QX-34-L': A QuantumInspire QX emulator running on Lisa SurfSara backend.
            'Spin-2': A QuantumInspire Spin-2 hardware backend
            'Starmon-5': A QuantumInspire Starmon-5 hardware backend.

            Default is 'QX single-node simulator'
        shots (int): number of circuit evaluations/random samples used to estimate expectation values and
            variances of observables.
            The maximum number of shots for the Quantum Inspire backends are:
            'QX single-node simulator': 4096
            'QX-34-L': 4096
            'Spin-2': 4096
            'Starmon-5': 16384

            Default number of shots is 1024.

    Keyword Args:
        token (str): The Quantum Inspire API token. If not provided or stored earlier, the environment
            variable ``QI_TOKEN`` is used.
        project (str): Name of the project as stored by Quantum Inspire.
    """

    name = "PennyLane Quantum Inspire plugin"
    short_name = "quantuminspire.qi"
    version = __version__
    author = "QuTech"

    # Set of backend names that define the backends that support returning the underlying quantum statevector
    _state_backends: Set[str] = set()

    _capabilities = {
        "model": "qubit",
        "supports_tensor_observables": True,
        "supports_inverse_operations": True,
        "supports_tracker": False,
        "returns_state": False,
    }
    # _operation_map = {**QISKIT_OPERATION_MAP, **QISKIT_OPERATION_INVERSES_MAP}
    #
    # operations = set(_operation_map.keys())
    # observables = {"PauliX", "PauliY", "PauliZ", "Identity", "Hadamard", "Hermitian", "Projector"}
    #
    # hw_analytic_warning_message = (
    #     "The analytic calculation of expectations, variances and "
    #     "probabilities is only supported on statevector backends, not on the {}. "
    #     "Such statistics obtained from this device are estimates based on samples."
    # )

    def __init__(
        self,
        wires: Union[int, Iterable[int], Iterable[str]],
        backend: str = "QX single-node simulator",
        shots: int = 1024,
        **kwargs: Dict[str, Any],
    ):
        # Connection to Quantum Inspire
        self._connect(kwargs)
        self._check_backend(backend, wires, shots)
        # Remove unsupported operations from base class
        unsupported_operations = []
        for operation in self.operations:
            if "QubitStateVector" in operation:
                unsupported_operations.append(operation)

        for unsupported_operation in unsupported_operations:
            self.operations.remove(unsupported_operation)
            del self._operation_map[unsupported_operation]

        # Initialize base class
        super().__init__(wires=wires, provider=QI, backend=backend, shots=shots, **kwargs)

    @staticmethod
    def _check_backend(backend: str, wires: Union[int, Iterable[int], Iterable[str]], shots: Optional[int]) -> None:
        """Check if the backend is valid and the wires and shots are valid
        Args:
            backend: the desired backend
            wires: Number of subsystems represented by the device,
                or iterable that contains unique labels for the subsystems as numbers (i.e., ``[-1, 0, 2]``)
                or strings (``['ancilla', 'q1', 'q2']``). Note that for some backends, the number
                of wires has to match the number of qubits accessible.
            shots: number of circuit evaluations/random samples used to estimate expectation values and
                variances of observables.

        """
        backend_type: Dict[str, Any] = QI.get_api().get_backend_type(backend)

        if shots is not None:
            if shots < 1:
                raise DeviceError("The specified number of shots needs to be > 0")
            elif shots > backend_type["max_number_of_shots"]:
                raise DeviceError(f'Invalid number of shots: {shots}. Must be <= {backend_type["max_number_of_shots"]}')

        if shots is not None and (shots < 1 or shots > backend_type["max_number_of_shots"]):
            raise DeviceError(f"Invalid number of shots: {shots}")

        if isinstance(wires, int):
            number_of_wires = wires
        else:
            number_of_wires = len(Wires(wires))

        if number_of_wires < 1 or number_of_wires > backend_type["number_of_qubits"]:
            raise DeviceError(f"Invalid number of wires: {number_of_wires}")

        if backend_type["is_hardware_backend"] and number_of_wires != backend_type["number_of_qubits"]:
            raise DeviceError(
                f"Invalid number of wires: {number_of_wires}. " f'Should be exactly {backend_type["number_of_qubits"]}'
            )

    @staticmethod
    def _connect(kwargs: Dict[str, Any]) -> None:
        """Function that allows connection to Quantum Inspire.

        Args:
            kwargs(dict): dictionary that contains the Quantum Inspire access token and project name
        """
        token = kwargs.get("token", None) is not None or load_account()
        date_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
        project_name = kwargs.get("project", f"PennyLane project {date_time}")

        qi_authentication = get_token_authentication(token)
        QI.set_authentication(qi_authentication, project_name=project_name)


def backend_online(backend: Backend) -> bool:
    """Check if backend is online for running experiments
    Args:
        backend: backend to check for being online
    """
    backend_type = QI.get_api().get_backend_type_by_name(backend.name())
    status = backend_type["status"]
    return bool(status != "OFFLINE")
