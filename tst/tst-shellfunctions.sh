#!/bin/bash
set -e

# Set some global variables for current test script and directory
prog=`basename $0`
dir=`dirname $0`

source $dir/../lib/shellfunctions.sh

# TODO: Provide a real unit test for this!
# Test #1:
declare params=`get_environment_from_file $dir/../data/tst.config tst`
echo "Expect: ' -username heinz -password geheim'"
echo "Result: '$params'"

# Test #2:
declare params=`get_environment_from_file $dir/../data/tst.config yyy`
echo "Expect: ' -username 123 -password 456'"
echo "Result: '$params'"
