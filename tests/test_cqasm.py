from unittest.mock import patch

import pennylane as qml
from pytest_mock import MockerFixture
from qiskit_quantuminspire.qi_backend import QIBackend

from pennylane_quantuminspire.cqasm import dumps
from pennylane_quantuminspire.qi_instructions import Asm

with patch("qiskit_quantuminspire.qi_provider.QIProvider"):
    from pennylane_quantuminspire.qi_device import QIDevice


def test_dumps(mocker: MockerFixture, QI_backend: QIBackend) -> None:
    device = QIDevice(backend=QI_backend)

    @qml.qnode(device=device)
    def quantum_function():  # type: ignore
        qml.Hadamard(wires=[0])
        Asm("TestBackend", """ a ' " {} () [] b """)
        return qml.expval(qml.PauliX(wires=[0]))

    expected_cqasm = (
        "version 3.0\n\n"
        "qubit[1] q\n"
        "bit[1] b\n\n"
        "H q[0]\n"
        "asm(TestBackend) ''' a ' \" {} () [] b '''\n"
        "H q[0]\n"
        "b[0] = measure q[0]\n"
    )

    assert dumps(quantum_function) == expected_cqasm
