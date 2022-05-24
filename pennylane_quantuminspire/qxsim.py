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
This module contains the :class:`~.QXSimDevice` class, a PennyLane device for the QuantumInspire QX single-node
emulator backend.
"""

from pennylane_quantuminspire.qi_device import QuantumInspireDevice


class QXSimDevice(QuantumInspireDevice):
    """A PennyLane device for the QuantumInspire QX single-node emulator backend.

    For more details, see the `Quantum Inspire documentation <https://github.com/QuTech-Delft/quantuminspire>`_

    You need to register at `Quantum Inspire <https://www.quantum-inspire.com/>`_ in order to
    receive a token that is used for authentication using the API.

    Args:
        wires (int or Iterable[Number, str]]): Number of subsystems represented by the device,
            or iterable that contains unique labels for the subsystems as numbers (i.e., ``[-1, 0, 2]``)
            or strings (``['ancilla', 'q1', 'q2']``). Note that for some backends, the number
            of wires has to match the number of qubits accessible.
        shots (int): number of circuit evaluations/random samples used to estimate expectation values and
            variances of observables.
            Currently the maximum number of shots is 4096 for QX single-node emulator backend.

    Keyword Args:
        token (str): The Quantum Inspire API token. If not provided or stored earlier, the environment
            variable ``QI_TOKEN`` is used.
        project (str): Name of the project as stored by Quantum Inspire.
    """

    short_name = "quantuminspire.qxsim"

    def __init__(self, wires, shots=1024, **kwargs):
        super().__init__(wires=wires, backend="QX single-node simulator", shots=shots, **kwargs)
