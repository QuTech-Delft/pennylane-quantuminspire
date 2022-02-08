import numpy as np
import pytest

import pennylane as qml
from pennylane_qiskit import AerDevice
from pennylane_quantuminspire.basic_device import QIDevice


class TestProbabilities:
    """Tests for the probability function"""

    def test_probability_no_results(self):
        """Test that the probabilities function returns
        None if no job has yet been run."""
        dev = QIDevice(backend="QX single-node simulator", wires=1, shots=None)
        assert dev.analytic_probability(wires=1) is None

