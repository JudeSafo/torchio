#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md', encoding='utf8') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst', encoding='utf8') as history_file:
    history = history_file.read()

requirements = [
    'Deprecated',
    'SimpleITK!=2.0.*',  # https://github.com/SimpleITK/SimpleITK/issues/1239
    'click',
    'humanize',
    'nibabel',
    'numpy>=1.15',
    'scipy',
    'torch>=1.1',
    'tqdm',
]


setup(
    author='Fernando Perez-Garcia',
    author_email='fepegar@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Typing :: Typed',
    ],
    description=(
        'Tools for loading, augmenting and writing 3D medical images'
        ' on PyTorch.'
    ),
    entry_points={
        'console_scripts': [
            'torchio-transform=torchio.cli.apply_transform:main',
            'tiotr=torchio.cli.apply_transform:main',
            'tiohd=torchio.cli.print_info:main',
        ],
    },
    extras_require={
        'plot': ['matplotlib'],
    },
    install_requires=requirements,
    license='Apache license',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='torchio',
    name='torchio',
    package_data={'torchio': ['py.typed']},
    packages=find_packages(include=['torchio', 'torchio.*']),
    setup_requires=[],
    test_suite='tests',
    tests_require=[],
    url='https://github.com/fepegar/torchio',
    version='0.18.75',
    zip_safe=False,
)
