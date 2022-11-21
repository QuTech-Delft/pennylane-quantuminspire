import numpy as np
import pytest

import pennylane as qml


@pytest.mark.usefixtures("online")
class TestCircuit:
    """Test simple RY circuit"""

    dev = qml.device(
        "quantuminspire.qi",
        wires=5,
        backend="Starmon-5",
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
