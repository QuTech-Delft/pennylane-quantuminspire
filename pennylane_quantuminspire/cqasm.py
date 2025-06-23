from typing import Any

import pennylane as qml
from pennylane_qiskit.converter import circuit_to_qiskit
from qiskit import QuantumCircuit
from qiskit_quantuminspire import cqasm


def convert_to_qiskit(q_node: qml.QNode, *args: Any, **kwargs: Any) -> QuantumCircuit:
    """Return the QiskitCircuit representation of the quantum function."""

    q_node.construct(args=args, kwargs=kwargs)

    used_wires = set()
    for op in q_node.qtape.operations:
        used_wires.update(op.wires)

    register_size = len(used_wires)

    quantum_circuit = circuit_to_qiskit(
        q_node.qtape,
        register_size=register_size,
    )
    return quantum_circuit


def dumps(q_node: qml.QNode, *args: Any, **kwargs: Any) -> str:
    """Return the cQASM representation of the quantum function."""
    quantum_circuit = convert_to_qiskit(q_node, *args, **kwargs)
    result: str = cqasm.dumps(quantum_circuit)
    return result
