import argparse

import pennylane as qml
from pennylane import numpy as np
from qiskit_quantuminspire.qi_provider import QIProvider

from pennylane_quantuminspire2.qi_device import QI2Device


def _run_e2e_tests(backend_name: str) -> None:
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


def main(name: str) -> None:
    _run_e2e_tests(backend_name=name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run E2E test on a backend.")
    parser.add_argument(
        "name",
        type=str,
        help="Name of the backend where the E2E tests will run.",
    )

    args = parser.parse_args()
    main(args.name)
