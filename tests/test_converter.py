import sys
import pytest

from pennylane_quantuminspire.converter import load_cqasm, load_cqasm_from_file
from pennylane.wires import Wires


@pytest.mark.skip(reason="conversion of cQASM to Qasm not yet implemented")
class TestConvertercQASM:
    """Tests that the converter.load function allows conversion from cQASM."""

    qft_cqasm = (
        "version 1.0"
        "qubits 4"
        "x q[0]"
        "x q[2]"
        "barrier q[0:3]"
        "h q[0]"
        "h q[1]"
        "h q[2]"
        "h q[3]"
        "measure q[0:3]"
    )

    @staticmethod
    @pytest.mark.skipif(sys.version_info < (3, 6), reason="tmpdir fixture requires Python >=3.6")
    def test_cqasm_from_file(tmpdir, recorder):
        """Tests that a QuantumCircuit object is deserialized from a cQASM file."""
        qft_cqasm = tmpdir.join("qft.cq")

        with open(qft_cqasm, "w", encoding="utf-8") as f:
            f.write(TestConvertercQASM.qft_cqasm)

        quantum_circuit = load_cqasm_from_file(qft_cqasm)

        with pytest.warns(UserWarning) as record:
            with recorder:
                quantum_circuit()

        assert len(recorder.queue) == 6

        assert recorder.queue[0].name == "PauliX"
        assert recorder.queue[0].parameters == []
        assert recorder.queue[0].wires == Wires([0])

        assert recorder.queue[1].name == "PauliX"
        assert recorder.queue[1].parameters == []
        assert recorder.queue[1].wires == Wires([2])

        assert recorder.queue[2].name == "Hadamard"
        assert recorder.queue[2].parameters == []
        assert recorder.queue[2].wires == Wires([0])

        assert recorder.queue[3].name == "Hadamard"
        assert recorder.queue[3].parameters == []
        assert recorder.queue[3].wires == Wires([1])

        assert recorder.queue[4].name == "Hadamard"
        assert recorder.queue[4].parameters == []
        assert recorder.queue[4].wires == Wires([2])

        assert recorder.queue[5].name == "Hadamard"
        assert recorder.queue[5].parameters == []
        assert recorder.queue[5].wires == Wires([3])

    @staticmethod
    def test_cqasm_file_not_found_error():
        """Tests that an error is propagated, when a non-existing file is specified for parsing."""
        qft_cqasm = "some_cqasm_file.cq"

        with pytest.raises(FileNotFoundError) as exc_info:
            load_cqasm_from_file(qft_cqasm)

        assert str(exc_info.value) == '[Errno 2] No such file or directory: \'some_cqasm_file.cq\''

    @staticmethod
    def test_cqasm_string(recorder):
        """Tests that a QuantumCircuit object is deserialized from a cQASM string."""
        cqasm_string = (
            "version 1.0"
            "qubit 4"
            "x q[0]"
            "cnot q[2], q[0]"
            "measure q[0:3]"
        )

        quantum_circuit = load_cqasm(cqasm_string)

        with pytest.warns(UserWarning) as record:
            with recorder:
                quantum_circuit(params={})

        assert len(recorder.queue) == 2

        assert recorder.queue[0].name == "PauliX"
        assert recorder.queue[0].parameters == []
        assert recorder.queue[0].wires == Wires([0])

        assert recorder.queue[1].name == "CNOT"
        assert recorder.queue[1].parameters == []
        assert recorder.queue[1].wires == Wires([2, 0])
