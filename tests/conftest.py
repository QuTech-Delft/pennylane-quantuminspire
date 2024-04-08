# PennyLane-Quantum Inspire Plugin
#
# Copyright 2023 QuTech Delft
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

import pennylane as qml
from pennylane_quantuminspire.qi_device import backend_online


state_backends = []
hw_backends = ["Starmon-5", "Spin-2"]
sim_backends = ["QX single-node simulator"]

@pytest.fixture(scope="class")
def online(request):
    if not backend_online(request.cls.dev.backend):
        pytest.skip("Skipping test, backend not online")

    return True


@pytest.fixture(params=state_backends + hw_backends + sim_backends)
def backend(request):
    return request.param


@pytest.fixture(params=hw_backends)
def hardware_backend(request):
    return request.param


@pytest.fixture(params=sim_backends)
def simulator_backend(request):
    return request.param


@pytest.fixture(scope="function")
def recorder():
    return qml.tape.OperationRecorder()
