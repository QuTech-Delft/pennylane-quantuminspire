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
This module contains functions for converting QuantumInspire cQASM programs
(via qasm) into PennyLane circuit templates.
"""
from typing import Any
from qiskit import QuantumCircuit
from pennylane_qiskit import load


def convert_cqasm_to_qasm(cqasm_string: str) -> str:
    """Converts a cQASM program to a OpenQASM 2.0 program.
    Args:
        cqasm_string: the cQASM string
    Returns:
        function: the OpenQASM 2.0 program as string
    """
    raise NotImplementedError


def load_cqasm(cqasm_string: str) -> Any:
    """Loads a PennyLane template from a cQASM string.
    Args:
        cqasm_string: the cQASM algorithm as a string
    Returns:
        function: the new PennyLane template
    """
    qasm_string = convert_cqasm_to_qasm(cqasm_string)
    return load(QuantumCircuit.from_qasm_str(qasm_string))


def load_cqasm_from_file(cqasm_file: str) -> Any:
    """Loads a PennyLane template from a cQASM file.
    Args:
        cqasm_file: the name of the cQASM file
    Returns:
        function: the new PennyLane template
    """
    with open(cqasm_file, "r", encoding="utf-8") as fh:
        cqasm_string = fh.read()

    qasm_string = convert_cqasm_to_qasm(cqasm_string)
    return load(QuantumCircuit.from_qasm_str(qasm_string))
