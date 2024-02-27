#!/bin/bash
pip3 install setuptools==44.1.0
pip3 install virtualenv
rm -rf docker_rm
python3 -m virtualenv docker_rm
source docker_rm/bin/activate

pip3 install -r requirement.txt

pytest -s -v

deactivate
