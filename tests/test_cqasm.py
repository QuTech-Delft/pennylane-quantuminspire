from unittest.mock import patch

import pennylane as qml
from pytest_mock import MockerFixture
from qiskit_quantuminspire.qi_backend import QIBackend

from pennylane_quantuminspire.cqasm import dumps

with patch("qiskit_quantuminspire.qi_provider.QIProvider"):
    from pennylane_quantuminspire.qi_device import QIDevice


def test_device_backends(mocker: MockerFixture, QI_backend: QIBackend) -> None:
    device = QIDevice(backend=QI_backend)

    @qml.qnode(device=device)
    def quantum_function():  # type: ignore
        qml.Hadamard(wires=[0])
        return qml.expval(qml.PauliX(wires=[0]))

    expected_cqasm = "version 3.0\n\nqubit[1] q\nbit[1] b\n\nH q[0]\nH q[0]\nb[0] = measure q[0]\n"

    assert dumps(quantum_function) == expected_cqasm
