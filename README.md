deployit-snippets
=================

This project contains some snippets for XebiaLabs DeployIt, e.g., command line and jython scripts.

Improved command line script
----------------------------

The default DeployIt CLI (shell) startup script has two drawbacks:
- On cygwin based environments it did not properly call Java: The JAR pathes need to be Windows path names (i.e. with Drive letter etc.), separated by ';' instead of ':'
- It performs a "cd" (Change Directory) command internally and therefor cannot handle relative paths, for, e.g., Jython scripts which should be executed on the server side.

The version in "bin/deployit-cli.sh" circumvents these two problems.

Additionally the extended cli tries to read a .netrc (see ftp(1)) like configuration with a machine/username/password triple to determine the application credentials.
The file is configured via the DEPLOYIT_CLI_NETRC environment variable. Make sure it has a strict list of
 machine xxx
 username yyy
 password zzz
triples! Despite standard ftp client .netrc a default section is prohibited!

Eval-POM
---------

The script _bin/eval-pom_ just provides a small helper to derive Maven 
POM parameters into the current environment.