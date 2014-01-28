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

# Try to determine additional parameters from $DEPLOYIT_CLI_RC and $DEPLOYIT_CLI_ENV
: ${DEPLOYIT_CLI_RC:="$HOME/.deployitrc"}

# Default params from RC file is empty
declare environment_params=''
if [ -n "${DEPLOYIT_CLI_ENV}" -a -n "${DEPLOYIT_CLI_RC}" -a -r "${DEPLOYIT_CLI_RC}" ]
   then environment_params=`get_environment_from_file ${DEPLOYIT_CLI_RC} ${DEPLOYIT_CLI_ENV}`
fi

exec $javacmd ${DEPLOYIT_CLI_OPTS} -classpath "${deployit_cli_classpath}" com.xebialabs.deployit.cli.Cli ${environment_params} "$@"
