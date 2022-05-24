# PennyLane-QuantumInspire

[![License](https://img.shields.io/github/license/qutech-delft/pennylane-quantuminspire.svg?)](https://opensource.org/licenses/Apache-2.0)

The PennyLane-QuantumInspire plugin integrates the QuantumInspire Quantum Computing backends
with PennyLane's quantum machine learning capabilities.

[PennyLane](https://pennylane.readthedocs.io/en/stable/) is a cross-platform Python library for quantum machine
learning, automatic differentiation, and optimization of hybrid quantum-classical computations.

[QuantumInspire](https://www.quantum-inspire.com/) is a platform for quantum computing developed by QuTech.

This plugin relies heavily on the [PennyLane-Qiskit Plugin](https://github.com/PennyLaneAI/pennylane-qiskit) for Qiskit.

[Qiskit](https://qiskit.org/documentation/) is an open-source framework for quantum computing.

## Features
Grants access to Quantum Inspire's cloud quantum [emulators](https://www.quantum-inspire.com/kbase/emulator-backends/)
and [hardware backends](https://www.quantum-inspire.com/kbase/hardware-backends/).

Emulators:
- QX single-node simulator
- QX-31 [requires advanced account]
- QX-34-L [requires advanced account]

Hardware:
- Spin-2
- Starmon-5

## Installation
This plugin requires Python version 3.7 and above, as well as PennyLane-Qiskit. Installation of the dependencies can be done using `pip`:

```
pip install pennylane-quantuminspire
```

To ensure your device is working as expected, you can install it in developer mode using `pip install -e pluginpath`, where `pluginpath` is the location of the plugin. It will then be accessible via PennyLane.

Furthermore, the plugin assumes Quantum Inspire credentials are stored on your disk in the default location. A token can be set using the following steps

1. Create a Quantum Inspire account if you do not already have one.
2. Get an API token from the Quantum Inspire website.
3. With your API token run:
```python
from quantuminspire.credentials import save_account
save_account('YOUR_API_TOKEN')
```
After calling save_account(), your credentials will be stored on disk.
Those who do not want to save their credentials to disk should use instead:
```python
from quantuminspire.credentials import enable_account
enable_account('YOUR_API_TOKEN')
```
and the token will only be active for the session.

After calling save_account() once or enable_account() within your session, token authentication is done automatically.

More information on different accounts can be found [here](https://www.quantum-inspire.com/kbase/accounts/#account-privileges).


## Getting started

Once the PennyLane-QuantumInspire plugin is installed, the provided Quantum Inspire devices can be accessed straight away in PennyLane.

The devices can be instantiated as follows:

```python
import pennylane as qml
dev = qml.device('quantuminspire.qidevice', wires=2, backend = "QX single-node simulator")
```

These devices can then be used just like other devices for the definition and evaluation of QNodes within the PennyLane framework.
