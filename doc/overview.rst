PennyLane-QuantumInspire Plugin
###############################

:Release: |release|

.. include:: ../README.rst
  :start-after:	header-start-inclusion-marker-do-not-remove
  :end-before: header-end-inclusion-marker-do-not-remove

Once the PennyLane-QuantumInspire plugin is installed and you have an API key, the Quantum Inspire device
can be accessed straightaway in PennyLane, without the need to import new packages.

Backends
~~~~~~~~

Currently, for the Quantum Inspire device four different backends are available:

.. title-card::
    :name: 'QX single-node simulator'
    :description: Quantum Inspire emulator run on a commodity cloud-based server, with 4GB RAM. It has a fast turn-around time for simulations up to 26 qubits. For basic users, the commodity cloud-based server will be sufficient.
    :link: backends/qxsim.html

.. title-card::
    :name: 'QX-34-L'
    :description: Quantum Inspire emulator runs on the Lisa cluster computer uses four nodes of the fat_soil_shared partition of Lisa. With 1.5TB of memory each, this allows simulation jobs of up to 34 qubits.
    :link: backends/qx34l.html

.. title-card::
    :name: 'Spin-2'
    :description: Quantum Inspire quantum 2-qubit semiconductor electron spin processor.
    :link: backends/spin2.html

.. title-card::
    :name: 'Starmon-5'
    :description: Quantum Inspire quantum 5-qubit superconductor Transmon processor.
    :link: backends/starmon5.html

.. raw:: html

    <div style='clear:both'></div>
    </br>

Selecting backends in Quantum Inspire device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Quantum Inspire backends specified in the previous section can be used by the Quantum Inspire device.
Selecting a specific backend for the Quantum Inspire device can be done by passing a ``backend`` argument with
the backend name:

.. code-block:: python

    dev = qml.device('quantuminspire.qi', wires=4, backend='QX single-node simulator')

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
Simply replace ``'default.qubit'`` with the Quantum Inspire device ``'quantuminspire.qi'`` and a backend of your choice,
such as ``'QX single-node simulator'``, or ``'QX-34-L'``.

.. raw:: html

    <br/>
