#!/bin/bash

if [[ -z $PYTHONPATH ]]; then
    export PYTHONPATH=.
fi

cd $(dirname $0)

if [ -f ./virtualenv/bin/activate ]; then
    . ./virtualenv/bin/activate
fi

python${1} ./codemitts/boot.py $@
