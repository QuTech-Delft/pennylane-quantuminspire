
import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

with open("pennylane_quantuminspire/_version.py") as f:
    VERSION = f.readlines()[-1].split()[-1].strip("\"'")

PACKAGE_NAME = 'pennylane_quantuminspire'
AUTHOR = 'Robert Wezeman'
AUTHOR_EMAIL = 'robert.wezeman@tno.nl'


DESCRIPTION = 'Pennylane plugin for QuantumInspire'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      "qiskit>=0.25",
      "pennylane_qiskit>=0.20.0",
      'quantuminspire>=1.7.0',
      'numpy',
]

DEVICES_LIST = [
        'quantuminspire.qidevice = pennylane_quantuminspire:QIDevice'
    ],

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages(),
      entry_points = {'pennylane.plugins': DEVICES_LIST}
      )