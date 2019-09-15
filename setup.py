#!/usr/bin/env python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "PyMLX90614",
    version = "0.0.1",
    author = "Connor Kneebone",
    author_email = "connor@sfxrescue.com",
    packages = setuptools.find_packages(exclude=['tests', 'notebooks']),
    description = "MLX90614 temperature sensor library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license = 'MIT',
    url = "https://github.com/Conr86/PyMLX90614",
    install_requires = [
        'smbus2',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)