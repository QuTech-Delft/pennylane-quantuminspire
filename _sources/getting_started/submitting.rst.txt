============================
How to: Submit a circuit
============================

Getting a backend
=================

Make sure you are logged into QI2, then use a QI2Device to fetch backends:

.. code-block:: python

    from qiskit_quantuminspire.qi_provider import QIProvider
    from pennylane_quantuminspire2.qi_device import QI2Device

    # Show all current supported backends:
    provider = QIProvider()
    for backend in provider.backends():
        print(f"{backend.name}")

    # Get Quantum Inspire's simulator backend:
    emulator_backend = provider.get_backend("QX emulator")

    # Instantiate a Pennylane device based on chosen backend
    demo_device = QI2Device(emulator_backend)


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
