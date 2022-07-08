The QX-34-L backend
===================

The ``'quantuminspire.qi'`` device hosts a QX Emulator instance on the Lisa cluster computer and uses four
nodes of the fat_soil_shared partition of Lisa. With 1.5TB of memory each, this allows simulation jobs of up to
34 qubits:

.. code-block:: python

    import pennylane as qml
    dev = qml.device('quantuminspire.qi', wires=14, backend='QX-34-L')

.. note::
    Choosing an emulator instance depends largely on the number of qubits that need to be simulated. Larger jobs require more resources. More resources means longer wait times to acquire the required resources.

    * Waiting time: minutes to hours
    * Maximum number of qubits: 34
    * Requires an advanced Quantum Inspire account
