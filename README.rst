PennyLane-QuantumInspire Plugin
###############################


.. image:: https://img.shields.io/github/license/qutech-delft/pennylane-quantuminspire.svg?
    :alt: License
    :target: https://opensource.org/licenses/Apache-2.0

.. image:: https://img.shields.io/readthedocs/pennylane-quantuminspire.svg?logo=read-the-docs&style=flat-square
    :alt: Read the Docs
    :target: https://pennylanequantuminspire.readthedocs.io

.. header-start-inclusion-marker-do-not-remove

The PennyLane-QuantumInspire plugin integrates the QuantumInspire Quantum Computing backends
with PennyLane's quantum machine learning capabilities.

`PennyLane <https://pennylane.readthedocs.io/en/stable/>`_ is a cross-platform Python library for quantum machine
learning, automatic differentiation, and optimization of hybrid quantum-classical computations.

`QuantumInspire <https://www.quantum-inspire.com/>`_ is a platform for quantum computing developed by QuTech.

This plugin relies heavily on the `PennyLane-Qiskit Plugin for Qiskit <https://github.com/PennyLaneAI/pennylane-qiskit>`_.

`Qiskit <https://qiskit.org/documentation/>`_ is an open-source framework for quantum computing.

.. header-end-inclusion-marker-do-not-remove

Features
========

Grants access to Quantum Inspire's cloud quantum `emulators <https://www.quantum-inspire.com/kbase/emulator-backends/>`_
and `hardware backends <https://www.quantum-inspire.com/kbase/hardware-backends/>`_.

Emulators:
* QX single-node simulator
* QX-34-L [requires advanced account]

Hardware:
* Spin-2
* Starmon-5

.. installation-start-inclusion-marker-do-not-remove

Installation
============

This plugin requires Python version 3.7 and above, as well as PennyLane-Qiskit. Installation of the dependencies can
be done using ``pip``:

.. code-block:: bash

    pip install pennylane-quantuminspire

To ensure your device is working as expected, you can install it in developer mode
using

.. code-block:: bash

    pip install -e pluginpath

where ``pluginpath`` is the location of the plugin. It will then be accessible via PennyLane.

Furthermore, the plugin assumes Quantum Inspire credentials are stored on your disk in the default location.
A token can be set using the following steps

1. Create a Quantum Inspire account if you do not already have one.
2. Get an API token from the Quantum Inspire website.
3. With your API token run:

.. code-block:: python

    from quantuminspire.credentials import save_account
    save_account('YOUR_API_TOKEN')

After calling save_account(), your credentials will be stored on disk.
Those who do not want to save their credentials to disk should use instead:

.. code-block:: python

   from quantuminspire.credentials import enable_account
   enable_account('YOUR_API_TOKEN')

and the token will only be active for the session.

After calling ``save_account()`` once or ``enable_account()`` within your session, token authentication is done
automatically.

More information on different accounts can be found `here <https://www.quantum-inspire.com/kbase/accounts/#account-privileges>`_.

Installing for generating documentation
=======================================

To install the necessary packages to perform documentation activities for this plugin do:

.. code-block:: bash

    pip install -e .[rtd]

The documentation generation process is dependent on pandoc. When you want to generate the
documentation and pandoc is not yet installed on your system navigate
to `Pandoc <https://pandoc.org/installing.html>`_ and follow the instructions found there to install pandoc.
To build the **readthedocs** documentation do:

.. code-block:: bash

    cd doc
    make html

The documentation is then build in '``doc/_build/html``'.

Getting started
===============

Once the PennyLane-QuantumInspire plugin is installed, the provided Quantum Inspire devices can be accessed straight
away in PennyLane.

The Quantum Inspire device can be instantiated with a QX single-node simulator backend as follows:

.. code-block:: python

    import pennylane as qml
    dev = qml.device('quantuminspire.qidevice', wires=2, backend = "QX single-node simulator")

This devices can then be used just like other devices for the definition and evaluation of QNodes within the
PennyLane framework.

.. installation-end-inclusion-marker-do-not-remove
.. support-start-inclusion-marker-do-not-remove

Support
=======

- **Source Code:** https://github.com/QuTech-Delft/pennylane-quantuminspire
- **Issue Tracker:** https://github.com/QuTech-Delft/pennylane-quantuminspire/issues
- **Quantum Inspire:** https://www.quantum-inspire.com/contact

If you are having issues, please let us know by posting the issue on our Github issue tracker. For questions about
Quantum Inspire see the contact info on the Quantum Inspire website.

.. support-end-inclusion-marker-do-not-remove
.. license-start-inclusion-marker-do-not-remove

License
=======

The PennyLane QuantumInspire plugin is **free** and **open source**, released under
the `Apache License, Version 2.0 <https://www.apache.org/licenses/LICENSE-2.0>`_.

.. license-end-inclusion-marker-do-not-remove
