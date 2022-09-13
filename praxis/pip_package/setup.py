# coding=utf-8
# Copyright 2022 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup.py file for praxis."""

from setuptools import setup, find_packages

setup(
    name='praxis',
    version='0.1.0',
    description=(
        'Functionalities such as a layers for building neural networks in Jax.'
    ),
    author='PAX team',
    author_email='pax-dev@google.com',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'protobuf', 'absl-py', 'fiddle', 'numpy', 'tensorflow', 'lingvo',
        'flax', 'jax', 'optax', 'optax-shampoo', 'jax-bitempered-loss',
        'einops', 't5x', 'clu'
    ],
    url='https://github.com/google/praxis',
    license='Apache-2.0',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    zip_safe=False,
)
