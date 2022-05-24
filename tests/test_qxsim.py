import numpy as np
import pytest

import pennylane as qml


class TestDevice:
    """Tests for the pennylane device"""

    def test_device(self):
        """
        """

        from pennylane.devices.tests import test_device
        test_device("quantuminspire.qxsim", shots=1024)


@pytest.mark.usefixtures("online")
class TestCircuit:
    """Test simple RY circuit"""

    dev = qml.device(
        "quantuminspire.qxsim",
        wires=2,
        shots=1024
    )

    @qml.qnode(dev)
    def circuit(theta):
        qml.RY(theta, wires=0)
        return qml.probs(wires=[0, 1])

    @pytest.mark.parametrize("theta", [0.512, 0.124, 1.23, 1.534, 0.662, 0])
    def test_circuit(self, theta):
        """Test if circuitRY close to exact result"""

        exact_outcome = np.array([np.cos(theta / 2) ** 2, 0, np.sin(theta / 2) ** 2, 0])
        probabilities = self.circuit(theta)
        assert np.linalg.norm(probabilities - exact_outcome) <= 0.08

    @qml.qnode(dev)
    def circuitH():
        qml.Hadamard(wires=1)
        return qml.probs(wires=[0, 1])

    def test_circuitH(self):
        """
        Test if circuitH close to exact result
        probabilities [|00> |01> |10> |11>] where |bit0 bit1>
        """
        exact_outcome = np.array([0.5, 0.5, 0, 0])
        probabilities = self.circuitH()
        assert np.linalg.norm(probabilities - exact_outcome) <= 0.06
