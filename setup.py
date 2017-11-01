from setuptools import setup

import bus_sdk

setup(
    name='bus_sdk',
    version=bus_sdk.__version__,
    description='SDK for the eLife Sciences bus - https://github.com/elifesciences/bus',
    packages=['bus_sdk'],
    license='MIT',
    url='https://github.com/elifesciences/bus-sdk-python.git',
    maintainer='eLife Sciences Publications Ltd.',
    maintainer_email='tech-team@elifesciences.org',
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
    ]
)
