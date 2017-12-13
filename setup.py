from setuptools import setup

import elife_bus_sdk


with open('requirements.txt') as f:
    install_requires = f.read().splitlines()


setup(
    name='elife_bus_sdk',
    version=elife_bus_sdk.__version__,
    description='SDK for the eLife Sciences bus - https://github.com/elifesciences/bus',
    packages=['elife_bus_sdk'],
    license='MIT',
    install_requires=install_requires,
    url='https://github.com/elifesciences/bus-sdk-python.git',
    maintainer='eLife Sciences Publications Ltd.',
    maintainer_email='tech-team@elifesciences.org',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
    ]
)
