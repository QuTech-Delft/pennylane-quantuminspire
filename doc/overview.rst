PennyLane-QuantumInspire Plugin
###############################

:Release: |release|

.. include:: ../README.rst
  :start-after:	header-start-inclusion-marker-do-not-remove
  :end-before: header-end-inclusion-marker-do-not-remove


Once the PennyLane-QuantumInspire plugin is installed and you have an API key, the QuantumInspire devices
can be accessed straightaway in PennyLane, without the need to import new packages.

Devices
~~~~~~~

Currently, there are three different devices available:

.. title-card::
    :name: 'quantuminspire.qxsim'
    :description: Quantum Inspire emulator run on a commodity cloud-based server, with 4GB RAM. It has a fast turn-around time for simulations up to 26 qubits. For basic users, the commodity cloud-based server will be sufficient.
    :link: devices/qxsim.html

.. title-card::
    :name: 'quantuminspire.qx34l'
    :description: Quantum Inspire emulator runs on the Lisa cluster computer uses four nodes of the fat_soil_shared partition of Lisa. With 1.5TB of memory each, this allows simulation jobs of up to 34 qubits.
    :link: devices/qx34l.html

.. title-card::
    :name: 'quantuminspire.spin2'
    :description: Quantum Inspire quantum 2-qubit semiconductor electron spin processor.
    :link: devices/spin2.html

.. title-card::
    :name: 'quantuminspire.starmon5'
    :description: Quantum Inspire quantum 5-qubit superconductor Transmon processor.
    :link: devices/starmon5.html

.. raw:: html

    <div style='clear:both'></div>
    </br>

For example, the ``'quantuminspire.qxsim'`` device with four wires is called like this:

.. code-block:: python

    import pennylane as qml
    dev = qml.device('quantuminspire.qxsim', wires=4)


Selecting backends via QuantumInspire device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The QuantumInspire device can have different **backends**. To select a specific backend to be used by the
QuantumInspire device is by specifying the backend by name. Both emulator and hardware backends can be selected
which is then used by the device. Selecting a certain backend for the QuantumInspire device can be done as follows:

.. code-block:: python

    dev = qml.device('quantuminspire.qi', wires=2, backend='Spin-2')

PennyLane chooses the ``QX single-node simulator`` as the default backend if no backend is specified.
For more details on the ``QX single-node simulator`` and the other emulator backends, including backend capacities, see
`Quantum Inspire Emulator backends documentation <https://www.quantum-inspire.com/kbase/emulator-backends/>`_.
For more details on the Quantum Inspire hardware backends, including operations specifics for the hardware backends,
see `Quantum Inspire Hardware backends documentation <https://www.quantum-inspire.com/kbase/hardware-backends/>`_.

Tutorials
~~~~~~~~~

You can try it out using any of the qubit based `demos from the PennyLane documentation
<https://pennylane.ai/qml/demonstrations.html>`_, for example the tutorial on
`qubit rotation <https://pennylane.ai/qml/demos/tutorial_qubit_rotation.html>`_.
Simply replace ``'default.qubit'`` with any of the available QuantumInspire devices,
such as ``'quantuminspire.qxsim'``, or ``'quantuminspire.qx34l'``.

.. raw:: html

    <br/>
