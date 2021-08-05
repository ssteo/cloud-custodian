# Automatically generated from poetry/pyproject.toml
# flake8: noqa
# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['c7n_kube',
 'c7n_kube.actions',
 'c7n_kube.resources',
 'c7n_kube.resources.apps',
 'c7n_kube.resources.core']

package_data = \
{'': ['*']}

install_requires = \
['argcomplete (>=1.12.3,<2.0.0)',
 'attrs (>=21.2.0,<22.0.0)',
 'boto3 (>=1.17.102,<2.0.0)',
 'botocore (>=1.20.102,<2.0.0)',
 'c7n (>=0.9.13,<0.10.0)',
 'importlib-metadata (>=4.6.0,<5.0.0)',
 'jmespath (>=0.10.0,<0.11.0)',
 'jsonschema (>=3.2.0,<4.0.0)',
 'kubernetes>=10.0.1,<11.0.0',
 'pyrsistent (>=0.18.0,<0.19.0)',
 'python-dateutil (>=2.8.1,<3.0.0)',
 'pyyaml (>=5.4.1,<6.0.0)',
 's3transfer (>=0.4.2,<0.5.0)',
 'six (>=1.16.0,<2.0.0)',
 'tabulate (>=0.8.9,<0.9.0)',
 'typing-extensions (>=3.10.0.0,<4.0.0.0)',
 'urllib3 (>=1.26.6,<2.0.0)',
 'zipp (>=3.4.1,<4.0.0)']

setup_kwargs = {
    'name': 'c7n-kube',
    'version': '0.2.12',
    'description': 'Cloud Custodian - Kubernetes Provider',
    'license': 'Apache-2.0',
    'classifiers': [
        'License :: OSI Approved :: Apache Software License',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Distributed Computing'
    ],
    'long_description': '# Custodian Kubernetes Support\n\n\nWork in Progress - Not Ready For Use.\n\n',
    'long_description_content_type': 'text/markdown',
    'author': 'Cloud Custodian Project',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://cloudcustodian.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
