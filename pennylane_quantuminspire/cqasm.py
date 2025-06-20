from typing import Any

import pennylane as qml
from qiskit import QuantumCircuit
from qiskit_quantuminspire import cqasm

from tests.simple import convert_to_qiskit


def dumps(q_node: qml.QNode, *args: Any, **kwargs: Any) -> str:
    """Return the cQASM representation of the quantum function."""

    q_node.construct(args=args, kwargs=kwargs)
    openqasm_code = q_node.tape.to_openqasm()

    # As of pennylane v0.40.0 Qnode.tape property is deprecated and instead the following approach is advised:
    # tape = qml.workflow.construct_tape(q_node)
    # openqasm_code = tape(*args, **kwargs).to_openqasm()

    quantum_circuit = QuantumCircuit.from_qasm_str(openqasm_code)
    result: str = cqasm.dumps(quantum_circuit)

    return result


def dumps_new(q_node: qml.QNode, *args: Any, **kwargs: Any) -> str:
    """Return the cQASM representation of the quantum function."""
    quantum_circuit = convert_to_qiskit(q_node, *args, **kwargs)
    result: str = cqasm.dumps(quantum_circuit)
    return result