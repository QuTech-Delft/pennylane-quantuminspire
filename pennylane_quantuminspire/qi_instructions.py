from pennylane.operation import Operation
from pennylane_qiskit.converter import QISKIT_OPERATION_MAP
from qiskit_quantuminspire.qi_instructions import Asm as QiskitQIAsm


class Asm(Operation):
    num_params = 2  # backend_name and asm_code
    num_wires = 0  # acts as a directive, not on wires
    par_domain = "A"  # "A" for any

    def __init__(self, backend_name: str = "", asm_code: str = "", id=None):
        super().__init__(backend_name, asm_code, wires=[], id=id)


PENNLYLANE_ASM_NAME = Asm().name
QISKIT_OPERATION_MAP[PENNLYLANE_ASM_NAME] = QiskitQIAsm
