import numpy as np
import pytest

import pennylane as qml


@pytest.mark.usefixtures("online")
class TestCircuit:
    """Test simple RY circuit"""

    dev = qml.device(
        "quantuminspire.qi",
        wires=2,
        backend="QX-34-L",
        shots=1024
    )

    @qml.qnode(dev)
    def circuit(theta):
        qml.RY(theta, wires=0)
        return qml.probs(wires=[0, 1])

    @pytest.mark.parametrize("theta", [0.512, 0.124, 1.23, 1.534, 0.662, 0])
    def test_circuit(self, theta):
        """
        Test if circuit runs and gives a result

        exact_outcome = np.array([np.cos(theta / 2) ** 2, 0, np.sin(theta / 2) ** 2, 0])
        np.linalg.norm(self.circuit(theta) - exact_outcome) should be small
        """
        assert isinstance(self.circuit(theta), (float, np.ndarray))

    @staticmethod
    @qml.qnode(dev)
    def circuitH():
        qml.Hadamard(wires=1)
        return qml.probs(wires=[0, 1])

    def test_circuitH(self):
        """
        Test if circuitH runs and gives a result
        probabilities [|00> |01> |10> |11>] where |bit0 bit1>

        exact_outcome = np.array([0.5, 0.5, 0, 0])
        np.linalg.norm(self.circuitH() - exact_outcome) should be small
        """
        assert isinstance(self.circuitH(), (float, np.ndarray))
