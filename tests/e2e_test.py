import argparse
import os

import pytest
import pennylane as qml
from pennylane import numpy as np
from qiskit_quantuminspire.qi_provider import QIProvider

from pennylane_quantuminspire.qi_device import QIDevice
from pennylane_quantuminspire.qi_instructions import Asm


@pytest.fixture
def backend_name() -> str:
    return os.getenv("BACKEND_NAME")


def test_complete_flow(backend_name: str) -> None:
    # Step 1: Create QML device
    provider = QIProvider()
    backend = provider.get_backend(backend_name)
    e2e_device = QIDevice(backend=backend)

    # Step 2: Create a quantum circuit
    @qml.qnode(e2e_device)
    def my_quantum_circuit(circuit_params):  # type: ignore
        qml.RX(circuit_params[0], wires=0)  # Apply an RX gate to qubit 0
        qml.RY(circuit_params[1], wires=1)  # Apply an RY gate to qubit 1
        qml.CNOT(wires=[0, 1])  # Apply a CNOT gate
        return qml.expval(qml.PauliZ(0))  # Measure the expectation value of PauliZ on qubit 0

    # Step 3: Initialize some parameters
    params = np.array([0.1, 0.2], requires_grad=True)

    # Step 4: Execute the circuit
    result = my_quantum_circuit(params)
    print(f"Params: {params}")
    print(f"Result: {result}")

    # Step 5: Perform optimization (optional)
    # For example, use gradient descent to minimize the output
    opt = qml.GradientDescentOptimizer(stepsize=0.1)
    params = opt.step(my_quantum_circuit, params)
    result = my_quantum_circuit(params)
    print(f"Optimized params: {params}")
    print(f"Optimized result: {result}")


def test_asm_decl(backend_name: str) -> None:
    provider = QIProvider()
    backend = provider.get_backend(backend_name)
    e2e_device = QIDevice(backend=backend)

    @qml.qnode(device=e2e_device)
    def quantum_function():  # type: ignore
        qml.Hadamard(wires=[0])
        Asm("TestBackend", """ a ' " {} () [] b """)
        return qml.expval(qml.PauliX(wires=[0]))

    result = quantum_function()
    print("Result asm decl:", result)
