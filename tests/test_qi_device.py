import numpy as np
import pytest

import pennylane as qml
from pennylane_quantuminspire.QI_device import QIDevice


class TestProbabilities:
    """Tests for the probability function"""

    def test_probability_no_results(self):
        """Test that the probabilities function returns
        None if no job has yet been run."""
        dev = QIDevice(backend="QX single-node simulator", wires=1, shots=None)
        assert dev.analytic_probability(wires=1) is None


class TestCircuit:
    """Test simple RY circuit"""

    dev = qml.device(
        "quantuminspire.qidevice",
        wires=2,
        shots=1024,
        backend="QX single-node simulator",
    )

    @qml.qnode(dev)
    def circuit(theta):
        qml.RY(theta, wires=0)
        return qml.probs(wires=[0, 1])

    @pytest.mark.parametrize("theta", [0.512, 0.124, 1.23, 1.534, 0.662, 0])
    def test_circuit(self, theta):
        """Test if circuit close to exact result"""

        exact_outcome = np.array([np.cos(theta / 2) ** 2, 0, np.sin(theta / 2) ** 2, 0])

        probabilities = self.circuit(theta)

        assert np.linalg.norm(probabilities - exact_outcome) <= 0.05
