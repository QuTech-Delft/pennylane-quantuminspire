from typing import Sequence

import pytest
from compute_api_client import BackendStatus, BackendType
from pytest_mock import MockerFixture
from qiskit_quantuminspire.qi_backend import QIBackend


def create_backend(id: int = 1, name: str = "qi_backend") -> QIBackend:
    backend_type = BackendType(
        name=name,
        nqubits=3,
        gateset=["x", "sdag", "prep_y", "measure_z", "h"],
        topology=[[0, 1], [1, 2], [2, 0]],
        id=id,
        is_hardware=True,
        image_id="qi_backend",
        features=[],
        default_compiler_config="",
        status=BackendStatus.IDLE,
        default_number_of_shots=1024,
        max_number_of_shots=2048,
        infrastructure="QCI",
        description="A Quantum Inspire backend",
        native_gateset="",
        supports_raw_data=False,
    )
    return QIBackend(backend_type=backend_type)


@pytest.fixture
def QI_backend(mocker: MockerFixture) -> QIBackend:
    """Backend fixture for fields we care about."""
    backend_object = create_backend()

    mock_property = mocker.PropertyMock(return_value=True)
    mocker.patch.object(type(backend_object), "available", mock_property)
    return backend_object


@pytest.fixture
def backend_repository() -> Sequence[BackendType]:
    return [
        create_backend(),
        create_backend(10, "qi_backend_10"),
    ]
