#!/bin/bash -x
#
# Demo script (adapt as required by your CI env & needs)
#
# You can extend this with args to:
# - specify only certain folders / files to lint
# - add a flag to lint only changed git files
# - specify rc file location
# - etc.
#
#

RCFILE="tools/pylint/.pylintrc"

pylint --rcfile=${RCFILE}  ./src

read -n1 -rp 'Press any key to continue'