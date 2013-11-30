#!/bin/bash

if [[ -z $PYTHONPATH ]]; then
    export PYTHONPATH=.
fi

if [ -f ./virtualenv/bin/activate ]; then
    . ./virtualenv/bin/activate
fi

python ./codemitts/loadtestdata.py
