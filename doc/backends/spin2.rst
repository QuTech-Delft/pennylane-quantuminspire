The Spin-2 backend
==================

The ``'quantuminspire.qi'`` device hosts a 2-qubit semiconductor electron spin processor with two qubits (q0, q1) which are connected:

.. code-block:: python

    import pennylane as qml
    dev = qml.device('quantuminspire.qi', wires=2, backend='Spin-2')

.. note::
    Currently the number of qubits to be used is **fixed** to 2.

    * Waiting time: seconds to minutes
    * Number of qubits: 2
