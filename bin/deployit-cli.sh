#!/bin/bash

# Abort if an error occurs
set -e

# Use the DEPLOYIT_CLI_HOME environment variable / or suitable default otherwise
# This might even be a symbolic link to the correct destination!
: ${DEPLOYIT_CLI_HOME:="/opt/deployit/cli-current"}
# Export it for the sake of sub processes

die () {
     msg=$1
     shift
     echo "$1" >&2
     exit 1
}

# Abort if the CLI Home does not exist
test ! -d "${DEPLOYIT_CLI_HOME}" && die "The Deployit CLI Home directory '${DEPLOYIT_CLI_HOME}' does not exist!"

# Set some global variables for current program and directory
prog=`basename $0`
dir=`dirname $0`

if test -d "$dir/../lib" -a -r "$dir/../lib/shellfunctions.sh"
   then source "$dir/../lib/shellfunctions.sh"
fi

# Remember: Shell variables (in opposite to ENVIRONMENT variables) are written in small letters!
if test -n "${JAVA_HOME}"
   then javacmd="${JAVA_HOME}/bin/java"
   else javacmd=java
fi

# Compute the Operating System
: ${SYS_OS:=`(uname -o 2>/dev/null || uname -s) | tr [A-Z] [a-z]`}

test -z "${SYS_OS}" && die "Operating System cannot be determined!"

# Compute the path delimiter!
case "${SYS_OS}" in 
    cygwin*)    deployit_cli_classpath=`cygpath -w $DEPLOYIT_CLI_HOME/conf`
        ;;
    * )         deployit_cli_classpath="$DEPLOYIT_CLI_HOME/conf"
        ;;
esac

# Build the DeployIt Class Path from the contents from the CLI Home, but with absolute path names!

# Attention: This might fail if the overall expansion of all Jar pathes extends the maximum string length!
# In this case split up the misc jar selections and send in a patch!
for jar in $DEPLOYIT_CLI_HOME/hotfix/*.jar $DEPLOYIT_CLI_HOME/lib/*.jar $DEPLOYIT_CLI_HOME/plugins/*.jar
do
    case "${SYS_OS}" in 
        cygwin*)    path_delimiter=';'
                    deployit_cli_classpath="$deployit_cli_classpath;"`cygpath -w $jar`
            ;;
        * )         path_delimiter=':'
                    deployit_cli_classpath="$deployit_cli_classpath:$jar"
        ;;
    esac
done

# Try to determine username and password from $DEPLOYIT_CLI_NETRC
username=''
password=''
server='localhost'

declare options=""
# username_set=false
# password_set=false
while [ "$#" -gt 0 ]
do
    opt=$1
    shift
    if test "$opt" == "-username"
       then username=$1
            shift
    elif test "$opt" == "-password"
       then password=$1
            shift 
    elif test "$opt" == "-host"
       then servername=$1
            shift
       else options="$options $opt"
    fi
done

if test "$DEPLOYIT_CLI_NETRC" -a \
    -r "$DEPLOYIT_CLI_NETRC" \
    -a \( ! "$username" -o ! "$password" \)
   then declare username_password=`get_user_and_pass_from_file $DEPLOYIT_CLI_NETRC $servername`
        test "$username" || username=`echo $username_password | awk '{print $1}'`
        test "$password" || password=`echo $username_password | awk '{print $2}'`
fi
test "$username" && options="$options -username $username"
test "$password" && options="$options -password $password"
test "$servername" && options="$options -host $servername"

# if eval $username_set
#    then :
#    else test "$username" && options="$options -username $username"
# fi
# if eval $password_set
#    then :
#    else test "$password" && options="$options -password $password"
# fi

exec $javacmd ${DEPLOYIT_CLI_OPTS} -classpath "${deployit_cli_classpath}" com.xebialabs.deployit.cli.Cli $options
