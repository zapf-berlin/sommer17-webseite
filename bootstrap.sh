#!/bin/sh
hugo

virtualenv -p python3 virtualenv
source virtualenv/bin/activate
pip install -r scripts/requirements.txt
