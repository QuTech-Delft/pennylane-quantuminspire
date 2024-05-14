import pytest
from unittest import TestCase

import pennylane as qml


@pytest.mark.usefixtures("online")
class TestPennyLaneDeviceTest(TestCase):
    """Do the integration tests with use of pennylane test_device
    pl-device-test --device=quantuminspire.qi --tb=short --skip-ops --shots=4096
                   --device-kwargs backend='QX single-node simulator'
    """
    # check if the used backend is online
    qi_backend = "QX single-node simulator"
    dev = qml.device(
        "quantuminspire.qi",
        wires=2,
        backend=qi_backend,
        shots=1024
    )

    def test_device(self):
        """
        Test Quantum Inspire device with 'QX single-node simulator' backend
        Alternatively, the command line can be used: >pl-device-test --device quantuminspire.qi --shots 1024
        """
        from pennylane.devices.tests import test_device
        test_device(device_name="quantuminspire.qi", shots=4096, skip_ops=True, pytest_args=["--tb=short"],
                    backend=self.qi_backend)
