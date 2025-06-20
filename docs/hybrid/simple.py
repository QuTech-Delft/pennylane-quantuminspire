from typing import Any, Dict, List

import pennylane as qml
from pennylane import numpy as np
from qi2_shared.hybrid.quantum_interface import QuantumInterface
from qiskit_quantuminspire.hybrid.hybrid_backend import QIHybridBackend
from scipy.optimize import minimize

from pennylane_quantuminspire.qi_device import QIDevice
from pennylane_quantuminspire.helpers import convert_to_qiskit

resultstring = ""


def generate_circuit(device: QIDevice) -> qml.QNode:
    # Define a simple Hamiltonian
    H = qml.Hamiltonian([0.5, 0.3], [qml.PauliZ(0) @ qml.PauliZ(1), qml.PauliX(0) @ qml.PauliX(1)])

    @qml.qnode(device)
    def circuit(params):  # type: ignore
        qml.RY(params[0], wires=0)
        qml.RY(params[1], wires=1)
        qml.CNOT(wires=[0, 1])
        return qml.expval(H)

    return circuit

def execute(qi: QuantumInterface) -> None:

    backend = QIHybridBackend(qi)
    device = QIDevice(backend=backend)

    circuit = generate_circuit(device)
    initial_params = np.array([0.1, 0.2], requires_grad=True)

    def cost_function(params):  # type: ignore
        qiskit_circuit = convert_to_qiskit(circuit, params)
        result = backend.run(qiskit_circuit, shots=1024).result()
        counts = result.get_counts()
        expectation_value = sum([int(state, 2) * count for state, count in counts.items()]) / 1024
        return expectation_value

    optimizer = minimize(cost_function, initial_params, method="COBYLA", options={"maxiter": 100})

    opt_params = optimizer.x
    final_energy = optimizer.fun

    global resultstring
    resultstring = "Optimization complete.\n"
    resultstring += f"Final Energy = {final_energy:.6f}\n"
    resultstring += f"Optimal Parameters = {opt_params}\n"
    print(resultstring)


def finalize(list_of_measurements: List[Dict[str, Any]]) -> Dict[str, Any]:
    global resultstring
    return {
        "results": list_of_measurements,
        "resultstring": resultstring,
    }
