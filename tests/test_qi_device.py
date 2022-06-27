import pytest
from unittest import TestCase

import pennylane as qml
import qiskit.providers.aer.noise as noise

from pennylane_quantuminspire.qi_device import backend_online


class TestDevice(TestCase):
    """Tests with use of pennylane test_device"""

    def test_device(self):
        """
        Test Quantum Inspire device with 'QX single-node simulator' backend
        Alternatively, the command line can be used: >pl-device-test --device quantuminspire.qi --shots 1024
        """
        pytest.skip("Skipping test, run it from command line to see results")

        from pennylane.devices.tests import test_device
        test_device("quantuminspire.qi", backend="QX single-node simulator", shots=1024)


class TestProbabilities:
    """Tests for the probability function"""

    def test_probability_no_results(self, simulator_backend):
        """
        Test that the probabilities function returns None if no job has yet been run.
        """
        dev = qml.device("quantuminspire.qi", backend=simulator_backend, wires=1, shots=None)
        if not backend_online(dev.backend):
            pytest.skip("Skipping test, backend not online")

        assert dev.analytic_probability(wires=1) is None


class TestQuantumInspireBackendOptions(TestCase):
    """Test the backend options of QuantumInspire backends."""

    def test_backend_options_cleaned(self):
        """Test that the backend memory options is reset upon new qxsim device
        initialization."""
        dev = qml.device("quantuminspire.qi", wires=2, backend="QX single-node simulator", memory=False)
        if not backend_online(dev.backend):
            pytest.skip("Skipping test, backend not online")

        assert dev.backend.options.get("memory") is True

        dev2 = qml.device("quantuminspire.qi", wires=2, backend="QX single-node simulator")
        if not backend_online(dev2.backend):
            pytest.skip("Skipping test, backend not online")

        assert dev2.backend.options.get("memory") is True

    def test_backend_unsupported_options(self):
        """Test that an unsupported backend options triggers an Exception."""
        noise_model = noise.NoiseModel()
        bit_flip = noise.pauli_error([("X", 1), ("I", 0)])

        # Create a noise model where the RX operation always flips the bit
        noise_model.add_all_qubit_quantum_error(bit_flip, ["rx"])

        with pytest.raises(AttributeError) as exc_info:
            _ = qml.device("quantuminspire.qi", wires=2, backend="QX single-node simulator", noise_model=noise_model)

        assert str(exc_info.value) == 'Options field noise_model is not valid for this backend'


class TestAnalyticWarningHWSimulator(TestCase):
    """Tests the warnings for when the analytic attribute of a device is set to true"""

    def test_warning_raised_for_hardware_backend_analytic_expval(self, hardware_backend, recorder):
        """Tests that a warning is raised if the analytic attribute is true on
        hardware simulators when calculating the expectation"""

        with pytest.warns(UserWarning) as record:
            number_of_wires = 2 if hardware_backend == "Spin-2" else 5
            dev = qml.device("quantuminspire.qi", backend=hardware_backend, wires=number_of_wires, shots=None)

        if not backend_online(dev.backend):
            pytest.skip("Skipping test, backend not online")

        # check that 1 UserWarning was raised
        user_warnings = [x for x in record.list if isinstance(x.message, UserWarning)]
        assert len(user_warnings) == 1
        # check that the message matches
        assert (
            user_warnings[0].message.args[0] == "The analytic calculation of "
                                                "expectations, variances and probabilities is only supported on "
                                                "statevector backends, not on the {}. Such statistics obtained from "
                                                "this device are estimates based on samples.".format(dev.backend)
        )
