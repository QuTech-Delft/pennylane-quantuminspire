import io
import logging
import pytest
import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

import pennylane as qml
from pennylane import DeviceError
from quantuminspire.exceptions import ApiError, QiskitBackendError
from pennylane_quantuminspire.qi_device import backend_online, QI


class MockApi:
    @staticmethod
    def get_backend_type_by_name(backend_name):
        if backend_name == 'backend_offline':
            return {'status': 'OFFLINE'
                    }
        return {'status': 'IDLE'
                }

    @staticmethod
    def get_backend_type(backend):
        if backend == 'non_existing_backend':
            raise ApiError(f'Backend type with name {backend} does not exist!')
        elif backend == 'offline_backend':
            return {'max_number_of_shots': 8192,
                    'number_of_qubits': 5,
                    'is_hardware_backend': False,
                    'status': "OFFLINE"
                    }
        elif backend == 'Starmon-5':
            return {'max_number_of_shots': 8192,
                    'number_of_qubits': 5,
                    'is_hardware_backend': True,
                    'status': "IDLE"
                    }
        elif backend == 'Spin-2':
            return {'max_number_of_shots': 4096,
                    'number_of_qubits': 2,
                    'is_hardware_backend': True,
                    'status': "IDLE"
                    }
        elif backend == 'QX-34-L':
            return {'max_number_of_shots': 4096,
                    'number_of_qubits': 34,
                    'is_hardware_backend': False,
                    'status': "IDLE"
                    }
        else:
            return {'max_number_of_shots': 4096,
                    'number_of_qubits': 26,
                    'is_hardware_backend': False,
                    'status': "IDLE"
                    }


@patch.object(QI, 'set_authentication')
@patch.object(QI, 'get_api', return_value=MockApi())
class TestDeviceConfiguration(TestCase):
    """Tests the device configuration compatibility"""

    def test_not_existing_backend(self, *args):
        """
        Test backend exists.
        """
        with pytest.raises(ApiError) as exc_info:
            _ = qml.device("quantuminspire.qi", wires=2, backend="non_existing_backend")

        assert str(exc_info.value) == 'Backend type with name non_existing_backend does not exist!'

    def test_number_of_wires_less_than_number_of_qubits_hardware_backends_succeed(self, *args):
        """
        Test that number of wires < number of qubits of hardware backends is supported.
        """
        with patch('pennylane_quantuminspire.qi_device.QiskitDevice.__init__'):
            _ = qml.device("quantuminspire.qi", wires=2, backend="Starmon-5")

        with patch('pennylane_quantuminspire.qi_device.QiskitDevice.__init__'):
            _ = qml.device("quantuminspire.qi", wires=['q0'], backend="Spin-2")

    def test_not_supported_number_of_wires(self, *args):
        """
        Test wires.
        """
        with pytest.raises(DeviceError) as exc_info:
            _ = qml.device("quantuminspire.qi", wires=[], backend="QX single-node simulator")

        assert str(exc_info.value) == 'Invalid number of wires: 0'

        with pytest.raises(DeviceError) as exc_info:
            _ = qml.device("quantuminspire.qi", wires=58, backend="QX-34-L")

        assert str(exc_info.value) == 'Invalid number of wires: 58'

    def test_not_supported_number_of_shots(self, *args):
        """
        Test shots.
        """
        with pytest.raises(DeviceError) as exc_info:
            _ = qml.device("quantuminspire.qi", wires=2, backend="QX single-node simulator", shots=10000)

        assert str(exc_info.value) == 'Invalid number of shots: 10000. Must be <= 4096'

        with pytest.raises(DeviceError) as exc_info:
            _ = qml.device("quantuminspire.qi", wires=5, backend="QX-34-L", shots=0)

        assert str(exc_info.value) == 'The specified number of shots needs to be > 0'

        with patch('pennylane_quantuminspire.qi_device.QiskitDevice.__init__'):
            # shots=None is accepted when creating the device (though not supported by the backends currently)
            _ = qml.device("quantuminspire.qi", wires=5, backend="QX-34-L", shots=None)

    def test_backend_online(self, *args):
        """
        Test backend being online.
        """

        backend_mock = MagicMock()
        backend_mock.name = MagicMock(return_value='backend_online')

        assert backend_online(backend_mock)

    def test_backend_offline(self, *args):
        """
        Test backend being offline.
        """

        backend_mock = MagicMock()
        backend_mock.name = MagicMock(return_value='backend_offline')

        assert not backend_online(backend_mock)

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout, \
             patch('pennylane_quantuminspire.qi_device.QiskitDevice.__init__'):

            stream_handler = logging.StreamHandler(sys.stdout)
            logging.getLogger().addHandler(stream_handler)

            _ = qml.device("quantuminspire.qi", wires=2, backend="offline_backend")

            # Verify printed warning
            print_string = mock_stdout.getvalue()
            self.assertIn("The backend you selected is currently offline. Your program will be queued until the "
                          "backend becomes available again. As a consequence a longer execution time applies. "
                          "You may check the website of Quantum Inspire to find information about longer downtimes. "
                          "Sorry for the inconvenience.", print_string)
            logging.getLogger().removeHandler(stream_handler)
