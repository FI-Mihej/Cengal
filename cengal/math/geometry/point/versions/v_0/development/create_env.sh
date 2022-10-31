#!/bin/bash

SCRIPT=`realpath $BASH_SOURCE`
SCRIPTPATH=`dirname $SCRIPT`
WORKDIR=`realpath $SCRIPTPATH`
ROOT_DIR=`realpath $WORKDIR/../../../../../../..`

cd $WORKDIR

if [ ! -d $WORKDIR/venv ]; then
    mkdir -p $WORKDIR/venv;
fi
virtualenv -p python3 $WORKDIR/venv

echo "export PYTHONPATH=$ROOT_DIR:\$PYTHONPATH" >> $WORKDIR/venv/bin/activate

cd $WORKDIR/venv/bin
source activate

cd $WORKDIR
pip install -r ./requirements.txt
