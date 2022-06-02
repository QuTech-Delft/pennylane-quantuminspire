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
This module contains the :class:`~.Starmon5Device` class, a PennyLane device for the QuantumInspire Starmon-5 hardware
backend.
"""
from typing import Any, Dict, Iterable, Union

from pennylane_quantuminspire.qi_device import QuantumInspireDevice


class Starmon5Device(QuantumInspireDevice):
    """A PennyLane device for the QuantumInspire Starmon-5 hardware backend.

    For more details, see the `Quantum Inspire documentation <https://github.com/QuTech-Delft/quantuminspire>`_

    You need to register at `Quantum Inspire <https://www.quantum-inspire.com/>`_ in order to
    receive a token that is used for authentication using the API.

    Args:
        wires (int or Iterable[Number, str]): Number of subsystems represented by the device,
            or iterable that contains unique labels for the subsystems as numbers (i.e., ``[-1, 0, 2]``)
            or strings (``['ancilla', 'q1', 'q2']``). Note that for some backends, the number
            of wires has to match the number of qubits accessible.
            Currently this value is fixed for Starmon-5 backend and should be 5
        shots (int): number of circuit evaluations/random samples used to estimate expectation values and
            variances of observables.
            Currently the maximum number of shots is 16384 for Starmon-5 backend.

    Keyword Args:
        token (str): The Quantum Inspire API token. If not provided or stored earlier, the environment
            variable ``QI_TOKEN`` is used.
        project (str): Name of the project as stored by Quantum Inspire.
    """

    short_name = "quantuminspire.starmon5"

    def __init__(
        self,
        wires: Union[int, Iterable[int], Iterable[str]] = 5,
        shots: int = 1024,
        **kwargs: Dict[str, Any]
    ):
        super().__init__(wires=wires, backend="Starmon-5", shots=shots, **kwargs)
