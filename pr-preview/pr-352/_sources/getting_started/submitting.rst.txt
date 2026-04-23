============================
How to: Submit a circuit
============================

Getting a backend
=================

Make sure you are logged into Quantum Inspire, then use a QIDevice to fetch backends:

.. code-block:: python

    from qiskit_quantuminspire.qi_provider import QIProvider
    from pennylane_quantuminspire.qi_device import QIDevice

    # Show all current supported backends:
    provider = QIProvider()
    for backend in provider.backends():
        print(f"{backend.name}")

    # Get Quantum Inspire's simulator backend:
    emulator_backend = provider.get_backend("QX emulator")

    # Instantiate a Pennylane device based on chosen backend
    demo_device = QIDevice(emulator_backend)


Submitting a Circuit
====================

Once a device has been specified, it may be used to submit circuits.
For example, running a Bell State:

.. code-block:: python

    import pennylane as qml

    @qml.qnode(demo_device)
    def bell_state():
        qml.Hadamard(wires=0)
        qml.CNOT(wires=[0, 1])
        return [qml.expval(qml.Z(x)) for x in range(2)]

    # Execute the circuit
    result = bell_state()

    # Print expectation values
    print(result)

.. warning::
    Other measurements than :code:`qml.expval()` and :code:`qml.var()` are only supported for backends that support measurement results for individual shots.


Support for Assembly Declaration
================================

The ``pennylane-quantuminspire`` plugin also supports assembly declarations that can be used to add backend-specific (assembly) code to a Pennylane circuit.  
They are realized through an ``Asm`` instruction.

Example
-------

.. code-block:: python

    import pennylane as qml
    from pennylane_quantuminspire.qi_instructions import Asm

    @qml.qnode(demo_device)
    def quantum_function():
        qml.Hadamard(wires=0)
        Asm("TestBackend", """ a ' " {} () [] b """)
        return qml.expval(qml.PauliX(wires=[0]))

The corresponding ``cQASM`` that gets generated for this circuit looks like:

.. code-block:: none

    version 3.0

    qubit[1] q
    bit[1] b

    H q[0]
    asm(TestBackend) ''' a ' " {} () [] b '''
    H q[0]
    barrier q[0]
    b[0] = measure q[0]

See the `Assembly declaration <https://qutech-delft.github.io/cQASM-spec/latest/language_specification/statements/assembly_declaration.html>`_ documentation for more on ``asm`` instructions.
