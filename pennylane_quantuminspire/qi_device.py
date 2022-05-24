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

import time
from abc import ABC

from pennylane_qiskit.qiskit_device import QiskitDevice

from qiskit.providers.backend import BackendV1 as Backend

from quantuminspire.credentials import load_account, get_token_authentication
from quantuminspire.exceptions import ApiError
from quantuminspire.qiskit import QI

from ._version import __version__


class QuantumInspireDevice(QiskitDevice, ABC):
    """A PennyLane device for the QuantumInspire API (remote) backend.

    For more details, see the `Quantum Inspire documentation <https://github.com/QuTech-Delft/quantuminspire>`_

    You need to register at `Quantum Inspire <https://www.quantum-inspire.com/>`_ in order to
    receive a token that is used for authentication using the API.

    Args:
        wires (int or Iterable[Number, str]]): Number of subsystems represented by the device,
            or iterable that contains unique labels for the subsystems as numbers (i.e., ``[-1, 0, 2]``)
            or strings (``['ancilla', 'q1', 'q2']``). Note that for some backends, the number
            of wires has to match the number of qubits accessible.
        backend (str): the desired backend, default is "QX single-node simulator"
        shots (int): number of circuit evaluations/random samples used to estimate expectation values and
            variances of observables. The default number of shots is 1024 for Quantum Inspire backends.

    Keyword Args:
        token (str): The Quantum Inspire API token. If not provided or stored earlier, the environment
            variable ``QI_TOKEN`` is used.
        project (str): Name of the project as stored by Quantum Inspire.
    """

    name = "PennyLane Quantum Inspire plugin"
    short_name = "quantuminspire.qi"
    # pennylane_requires = ">=0.23.0"  # use default from QiskitDevice
    version = __version__
    author = "QuTech"

    # Set of backend names that define the backends that support returning the underlying quantum statevector
    _state_backends = {}

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

    def __init__(self, wires, backend="QX single-node simulator", shots=1024, **kwargs):
        # Connection to Quantum Inspire
        connect(kwargs)

        super().__init__(wires=wires, provider=QI, backend=backend, shots=shots, **kwargs)

        unsupported_operations = []
        for operation in self.operations:
            if "QubitStateVector" in operation:
                unsupported_operations.append(operation)

        for unsupported_operation in unsupported_operations:
            self.operations.remove(unsupported_operation)
            del self._operation_map[unsupported_operation]


def connect(kwargs):
    """Function that allows connection to Quantum Inspire.

    Args:
        kwargs(dict): dictionary that contains the Quantum Inspire access token and project name
    """
    token = kwargs.get("token", None) is not None or load_account()
    project_name = kwargs.get("project", f"pennylane_project_{int(time.time())}")

    qi_authentication = get_token_authentication(token)
    QI.set_authentication(qi_authentication, project_name=project_name)


def backend_online(backend):
    backend_type = QI.get_api().get_backend_type_by_name(backend.name())
    status = backend_type["status"]
    return status != "OFFLINE"


