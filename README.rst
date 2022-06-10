PennyLane-QuantumInspire Plugin
###############################

.. image:: https://img.shields.io/github/license/qutech-delft/pennylane-quantuminspire.svg?
    :alt: License
    :target: https://opensource.org/licenses/Apache-2.0

.. image:: https://img.shields.io/readthedocs/pennylane-quantuminspire.svg?logo=read-the-docs&style=flat-square
    :alt: Read the Docs
    :target: https://pennylane-quantuminspire.readthedocs.io

.. header-start-inclusion-marker-do-not-remove

The PennyLane-QuantumInspire plugin integrates the Quantum Inspire quantum computing backends
with PennyLane's quantum machine learning capabilities.

`PennyLane <https://pennylane.readthedocs.io/en/stable/>`_ is a cross-platform Python library for quantum machine
learning, automatic differentiation, and optimization of hybrid quantum-classical computations.

`Quantum Inspire <https://www.quantum-inspire.com/>`_ is a platform for quantum computing developed by QuTech.

This plugin relies heavily on the software development kit `(SDK) for the Quantum Inspire platform <https://github.com/QuTech-Delft/quantuminspire>`_
and the `PennyLane-Qiskit Plugin for Qiskit <https://github.com/PennyLaneAI/pennylane-qiskit>`_.

`Qiskit <https://qiskit.org/documentation/>`_ is an open-source framework for quantum computing.

The Quantum Inspire device is build on top of the Qiskit device. The Quantum Inspire SDK registers a Quantum Inspire
backend to Qiskit to run the algorithms on. This way we combine the strengths and ease of use of the Qiskit plugin
with the computing power of Quantum Inspire backends.

.. header-end-inclusion-marker-do-not-remove

Features
========

Grants access to Quantum Inspire's cloud quantum `emulators <https://www.quantum-inspire.com/kbase/emulator-backends/>`_
and `hardware backends <https://www.quantum-inspire.com/kbase/hardware-backends/>`_.

Emulator backends:

* ``"QX single-node simulator"`` - Quantum Inspire emulator run on a commodity cloud-based server, with 4GB RAM. It has a fast turn-around time for simulations up to 26 qubits. For basic users, the commodity cloud-based server will be sufficient.
* ``"QX-34-L"`` - Quantum Inspire emulator runs on the Lisa cluster computer uses four nodes of the fat_soil_shared partition of Lisa. With 1.5TB of memory each, this allows simulation jobs of up to 34 qubits [**requires advanced account**].

Hardware backends:

* ``"Spin-2"`` - Quantum Inspire quantum 2-qubit semiconductor electron spin processor.
* ``"Starmon-5"`` - Quantum Inspire quantum 5-qubit superconductor Transmon processor.

.. installation-start-inclusion-marker-do-not-remove

Installation
============

This plugin requires Python version 3.7 and above, as well as PennyLane-Qiskit. Installation of the dependencies can
be done using ``pip``:

.. code-block:: bash

    pip install pennylane-quantuminspire

To ensure your device is working as expected, you can also install the development version from source by cloning
this repository and running a pip install command in the root directory of the repository:

.. code-block:: bash

    git clone https://github.com/QuTech-Delft/pennylane-quantuminspire.git
    cd pennylane-quantuminspire
    pip install -e pluginpath

where ``pluginpath`` is the location of the plugin. It will then be accessible via PennyLane.

Furthermore, the plugin assumes Quantum Inspire credentials are stored on your disk in the default location.
A token can be set using the following steps:

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

The documentation can then be found in the '``doc/_build/html``' directory.

Installing for running tests
============================

Make sure to install test dependencies first:

.. code-block:: bash

    pip install -e .[dev]

Unit tests
~~~~~~~~~~

Run the unit tests using:

.. code-block:: bash

    pytest

or including coverage:

.. code-block:: bash

    pytest tests --cov=pennylane_quantuminspire --cov-report=term-missing --cov-report=xml -p no:warnings --tb=native

.. installation-end-inclusion-marker-do-not-remove

.. getting-started-start-inclusion-marker-do-not-remove

Getting started
===============

Once the PennyLane-QuantumInspire plugin is installed, the provided Quantum Inspire device can be accessed straight
away in PennyLane.

The Quantum Inspire device can be instantiated with a ``QX single-node simulator`` backend as follows:

.. code-block:: python

    import pennylane as qml
    dev = qml.device('quantuminspire.qi', wires=2, backend='QX single-node simulator')

This device can then be used just like other devices for the definition and evaluation of QNodes within the
PennyLane framework.

Inspecting results of computations in Quantum Inspire
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a computation has run on a Quantum Inspire backend the algorithm that was executed and the results can be
inspected in Quantum Inspire.
When algorithms are run on a backend of the Quantum Inspire device, all the executed algorithms are contained in a
single Quantum Inspire project.
After logging in to the `Quantum Inspire platform <https://www.quantum-inspire.com>`_ an overview is given of the
available projects. By opening your project the backend that computed the results is displayed. Navigating to
``Results`` show the computation results for each algorithm. Also the algorithms code can be inspected here.
The project name that is used by the plugin can be passed as a separate argument ``project`` to the Quantum
Inspire device constructor. For example:

.. code-block:: python

    dev = qml.device('quantuminspire.qi', wires=4, project='My project name')

When no project name is given the project name defaults to: ``'PennyLane project 2022-06-07 09:50:38'``, where the last
parts of the project name are replaced by the current date and local time.
More information about working with Quantum Inspire can be found at
`Quantum Inspire Quick Guide <https://www.quantum-inspire.com/kbase/quick-guide/>`_. Specific information about
managing projects can be found at
`Managing your projects <https://www.quantum-inspire.com/kbase/managing-your-projects/>`_.

.. getting-started-end-inclusion-marker-do-not-remove
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
