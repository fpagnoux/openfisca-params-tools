#! /usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name = "OpenFisca-Params-Tools",
    version = "0.1.0",
    author = "OpenFisca Team",
    author_email = "contact@openfisca.fr",
    classifiers = [],
    license = "http://www.fsf.org/licensing/licenses/agpl-3.0.html",
    data_files = [],
    extras_require = {},
    include_package_data = True,  # Will read MANIFEST.in
    install_requires = [],
    packages = find_packages(exclude=["tests*"]),
    )
