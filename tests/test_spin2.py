import numpy as np
import pytest

import pennylane as qml
from pennylane import DeviceError


@pytest.mark.usefixtures("online")
class TestCircuit:
    """Test simple RY circuit"""

    dev = qml.device(
        "quantuminspire.qi",
        wires=2,
        backend="Spin-2",
        shots=1024
    )

    @qml.qnode(dev)
    def circuit(theta):
        qml.RY(theta, wires=0)
        return qml.probs(wires=[0, 1])

    @pytest.mark.parametrize("theta", [0.512, 0.124, 1.23, 1.534, 0.662, 0])
    def test_circuit(self, theta):
        """
        Test if the circuit runs. Correctness of the result depends on the hardware used

        exact_outcome = np.array([np.cos(theta / 2) ** 2, 0, np.sin(theta / 2) ** 2, 0])
        np.linalg.norm(self.circuit(theta) - exact_outcome) should be small
        """
        assert isinstance(self.circuit(theta), (float, np.ndarray))


@pytest.mark.usefixtures("online")
class TestNumberOfWires:
    """Test provided wires."""

    dev = qml.device(
        "quantuminspire.qi",
        wires=2,
        backend="Spin-2"
    )

    @pytest.mark.parametrize("wires", [1, 2, [0], [0, 1]])
    def test_valid_wires(self, wires):
        """Test valid input wires"""
        dev = qml.device(
            "quantuminspire.qi", wires=wires, backend="Spin-2", shots=1024
        )

        @qml.qnode(dev)
        def circuit():
            """
            Test if the circuit runs. Correctness of the result depends on the hardware used.
            """
            qml.RY(0.512, wires=0)
            return qml.probs(wires=[0])

        assert isinstance(circuit(), (float, np.ndarray))

    @pytest.mark.parametrize("wires", [0, []])
    def test_zero_wires(self, wires):
        """Test empty input wires"""
        expected_message = "Invalid number of wires: 0"
        with pytest.raises(DeviceError, match=expected_message):
            qml.device(
                "quantuminspire.qi", wires=wires, backend="Spin-2", shots=1024
            )

    @pytest.mark.parametrize("wires", [3, [0, 1, 2]])
    def test_too_many_wires(self, wires):
        """Test too many input wires"""
        expected_message = f"Invalid number of wires: 3"
        with pytest.raises(DeviceError, match=expected_message):
            qml.device(
                "quantuminspire.qi", wires=wires, backend="Spin-2", shots=1024
            )
