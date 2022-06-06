The Starmon-5 device
====================

The ``'quantuminspire.starmon5'`` device hosts a 5-qubit superconductor Transmon processor with five qubits
connected in a X-shaped configuration. q2 is the central qubit and is connected to every other qubit.
All other qubits (q0, q1, q3, q4) couple to q2 only:

.. code-block:: python

    import pennylane as qml
    dev = qml.device('quantuminspire.starmon5', wires=5)

.. note::
    Currently the number of qubits to be used is fixed to 5.

    * Waiting time: seconds to minutes
    * Number of qubits: 5
