#!/bin/bash
set -e

# Set some global variables for current program and directory
prog=`basename $0`
dir=`dirname $0`

source $dir/../lib/shellfunctions.sh

# Usage/Test:
declare username_password=`get_user_and_pass_from_file $dir/../data/tst-netrc tst`
username=`echo $username_password | awk '{print $1}'`
password=`echo $username_password | awk '{print $2}'`
echo "Expect user 'heinz' and pass 'geheim'"
echo "User: '$username'"
echo "Pass: '$password'"
