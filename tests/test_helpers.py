from unittest.mock import patch

import pennylane as qml
from pytest_mock import MockerFixture
from qiskit_quantuminspire.qi_backend import QIBackend

from qiskit_quantuminspire import cqasm
from pennylane_quantuminspire.helpers import convert_to_qiskit
from pennylane_quantuminspire.qi_instructions import Asm

with patch("qiskit_quantuminspire.qi_provider.QIProvider"):
    from pennylane_quantuminspire.qi_device import QIDevice


def test_convert_to_qiskit(mocker: MockerFixture, QI_backend: QIBackend) -> None:
    device = QIDevice(backend=QI_backend)

    @qml.qnode(device=device)
    def quantum_function():  # type: ignore
        qml.Hadamard(wires=[0])
        Asm("TestBackend", """ a ' " {} () [] b """)
        return qml.expval(qml.PauliX(wires=[0]))

    qiskit_circuit = convert_to_qiskit(quantum_function)

    circuit_str = cqasm.dumps(qiskit_circuit)

    assert """asm(TestBackend) ''' a ' " {} () [] b '''""" in circuit_str
