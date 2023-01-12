# PennyLane-Quantum Inspire Plugin
#
# Copyright 2022 QuTech Delft
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

#!/usr/bin/env python3
from setuptools import setup

with open("pennylane_quantuminspire/_version.py", "r", encoding="utf-8") as f:
    version = f.readlines()[-1].split()[-1].strip("\"'")

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = [
    "pennylane-qiskit>=0.23.0",
    "quantuminspire>=2.0.0",
    "qiskit>=0.32.0",
]

extra_requirements = {
    'dev': ['pytest>=3.3.1', 'pytest-cov', 'pytest-mock', 'pylint', 'mypy>=0.670', 'black'],
    'rtd': ['docutils==0.19', 'ipykernel==6.19.2', 'jinja2==3.1.2', 'mthree==1.1.0', 'nbsphinx==0.8.11',
            'pybind11==2.10.3', 'pygments==2.13.0', 'pygments-github-lexers==0.0.5', 'sphinxcontrib-bibtex==2.5.0',
            'sphinx-automodapi==0.14.1', 'xanadu-sphinx-theme==0.3.5'],
}

devices_list = [
    'quantuminspire.qi = pennylane_quantuminspire:QuantumInspireDevice',
]

converters_list = [
    # 'cqasm = pennylane_quantuminspire:load_cqasm',
    # 'cqasm_file = pennylane_quantuminspire:load_cqasm_from_file',
]

info = {
    'name': 'pennylane-quantuminspire',
    'version': version,
    'author': 'QuTech',
    'author_email': 'robert.wezeman@tno.nl',
    'maintainer': 'QuTech SDST',
    'maintainer_email': 'software@qutech.support',
    'url': 'https://github.com/QuTech-Delft/pennylane-quantuminspire',
    'license': 'Apache License 2.0',
    'packages': [
        'pennylane_quantuminspire'
    ],
    'entry_points': {
        'pennylane.plugins': devices_list,
        'pennylane.io': converters_list
    },
    'description': 'PennyLane Plugin for Quantum Inspire',
    'long_description': long_description,
    'long_description_content_type': 'text/x-rst',
    'provides': ["pennylane_quantuminspire"],
    'install_requires': requirements,
    'extras_require': extra_requirements,
    'command_options': {
        'build_sphinx': {
            'version': ('setup.py', version),
            'release': ('setup.py', version)}}
}

classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: POSIX",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python",
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3 :: Only',
    "Topic :: Scientific/Engineering :: Physics"
]

setup(classifiers=classifiers, **info)
