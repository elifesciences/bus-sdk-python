#!/usr/bin/env bash
set -e

if [ ! -e "venv/bin/python3" ]; then
    echo "could not find venv/bin/python3, recreating venv"
    rm -rf venv
    virtualenv --python=python3 venv
fi

source venv/bin/activate

pip install -r requirements.txt
pip install -r requirements-dev.txt

coverage run -m pytest --junitxml=build/pytest.xml
