"""
This module contains the :class:`~.QIDevice` class, a PennyLane device that allows
evaluation and differentiation of Quantum Inspire's Quantum Processing Units (QPUs)
using PennyLane.
"""

from pennylane_qiskit.qiskit_device import QiskitDevice

from quantuminspire.qiskit import QI
import quantuminspire

import time
import os

from ._version import __version__


class QIDevice(QiskitDevice):
    """A PennyLane device for the QuantumInspire API (remote) backend.

    For more details, see the `QuantumInspire documentation <https://github.com/QuTech-Delft/quantuminspire>`_

    You need to register at `QI <https://https://www.quantum-inspire.com/>`_ in order to
    receive a token that is used for authentication using the API.

    Args:
        wires (int or Iterable[Number, str]]): Number of subsystems represented by the device,
            or iterable that contains unique labels for the subsystems as numbers (i.e., ``[-1, 0, 2]``)
            or strings (``['ancilla', 'q1', 'q2']``). Note that for some backends, the number
            of wires has to match the number of qubits accessible.
        backend (str): the desired backend
        shots (int): number of circuit evaluations/random samples used
            to estimate expectation values and variances of observables

    Keyword Args:
        qi_token (str): The QI API token. If not provided, the environment
            variable ``QI_TOKEN`` is used.
        project (str): Name of the project as stored by QI.
    """

    name = "Quantum Inspire PennyLane plugin"
    pennylane_requires = ">=0.20.0"
    version = __version__
    plugin_version = __version__
    author = "TNO"
    short_name = "quantuminspire.qidevice"

    _state_backends = {}

    def __init__(self, wires, shots=1024, backend="QX single-node simulator", **kwargs):

        # Connection to QI
        connect(kwargs)

        super().__init__(
            wires=wires, provider=QI, backend=backend, shots=shots, **kwargs
        )


def connect(kwargs):
    """Function that allows connection to QI.
    Args:
        kwargs(dict): dictionary that contains the QI access token and project name"""

    token = kwargs.get("token", None) or quantuminspire.credentials.load_account()
    project = kwargs.get("project", f"pennylane_project_{int(time.time())}")

    qi_authentication = quantuminspire.credentials.get_token_authentication(token)

    QI_URL = os.getenv("API_URL", "https://api.quantum-inspire.com/")
    QI.set_authentication(qi_authentication, QI_URL, project_name=project)
