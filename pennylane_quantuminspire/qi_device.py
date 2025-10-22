from typing import Any

from pennylane.devices.execution_config import DefaultExecutionConfig, ExecutionConfig
from pennylane.exceptions import DeviceError
from pennylane_qiskit import RemoteDevice
from pennylane_qiskit.qiskit_device import QuantumTape_or_Batch, Result_or_ResultBatch
from qiskit.exceptions import QiskitError
from qiskit_quantuminspire.qi_backend import QIBackend

from pennylane_quantuminspire.qi_instructions import PENNLYLANE_ASM_NAME


class QIDevice(RemoteDevice):  # type: ignore[misc]
    def __init__(self, backend: QIBackend, **kwargs: Any) -> None:
        super().__init__(wires=backend.num_qubits, backend=backend, **kwargs)
        self.operations.add(PENNLYLANE_ASM_NAME)

    # pylint: disable=unused-argument, no-member
    def execute(
        self,
        circuits: QuantumTape_or_Batch,
        execution_config: ExecutionConfig = DefaultExecutionConfig,
    ) -> Result_or_ResultBatch:
        try:
            results = super().execute(circuits, execution_config)
            return results
        except QiskitError as e:
            raise DeviceError(str(e)) from e
