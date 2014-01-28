#!/bin/bash
set -e

# Set some global variables for current program and directory
prog=`basename $0`
dir=`dirname $0`

source $dir/../lib/shellfunctions.sh

# Usage/Test:
declare params=`get_environment_from_file $dir/../data/tst.config tst`
echo "Expect '-username heinz -password geheim'"
echo "Params: '$params'"
