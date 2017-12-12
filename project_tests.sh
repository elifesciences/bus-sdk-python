#!/usr/bin/env bash
set -e

if [ ! -e "venv/bin/python3.5" ]; then
    echo "could not find venv/bin/python3.5, recreating venv"
    rm -rf venv
    virtualenv --python=python3.5 venv
fi

source venv/bin/activate

pip install --requirement requirements.txt
pip install coveralls
pip install proofreader==0.0.2

python -m proofreader elife_bus_sdk/ test/

coverage run -m pytest --junitxml=build/pytest.xml

COVERALLS_REPO_TOKEN=$(cat /etc/coveralls/tokens/elife-bus-sdk) coveralls
