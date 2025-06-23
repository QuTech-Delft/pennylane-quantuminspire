from typing import Any

from pennylane.operation import Operation
from pennylane_qiskit.converter import QISKIT_OPERATION_MAP
from qiskit_quantuminspire.qi_instructions import Asm as QiskitQIAsm


class Asm(Operation):  # type: ignore[misc]
    num_params = 2  # backend_name and asm_code
    num_wires = 0  # acts as a directive, not on wires
    par_domain = "A"  # "A" for any

    def __init__(self, backend_name: str = "", asm_code: str = "", id: Any | None = None):
        super().__init__(backend_name, asm_code, wires=[], id=id)


# This is a workaround to enable Asm instructions with the pennylane-quantuminspire plugin.
# The plugin only supports operations officially defined in Qiskit, and Asm is not one of them.
# Since this is not officially supported, we manually register a custom mapping to make it work.
PENNLYLANE_ASM_NAME = Asm().name
QISKIT_OPERATION_MAP[PENNLYLANE_ASM_NAME] = QiskitQIAsm
