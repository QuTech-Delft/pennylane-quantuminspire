The QXSim device
================

The ``'quantuminspire.qxsim'`` device hosts a QX Emulator instance on the a commodity cloud-based server, with 4GB RAM. It has a fast turn-around time for simulations up to 26 qubits.
For basic users, the commodity cloud-based server will be sufficient:

.. code-block:: python

    import pennylane as qml
    dev = qml.device('quantuminspire.qxsim', wires=10)


.. note::
    Choosing a emulator instance depends largely on the number of qubits that need to be simulated. Larger jobs require more resources. More resources means longer wait times to acquire the required resources.

    * Waiting time: seconds to minutes
    * Maximum number of qubits: 26
