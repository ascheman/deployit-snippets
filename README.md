deployit-snippets
=================

This project contains some snippets for XebiaLabs DeployIt, e.g., command line and jython scripts.

Improved command line script
----------------------------

The default DeployIt CLI (shell) startup script has two drawbacks:
- On cygwin based environments it did not properly call Java: The JAR pathes need to be Windows path names (i.e. with Drive letter etc.), separated by ';' instead of ':'
- It performs a "cd" (Change Directory) command internally and therefor cannot handle relative paths, for, e.g., Jython scripts which should be executed on the server side.

The version in "bin/deployit-cli.sh" circumvents these two problems.

Eval-POM
---------

The script _bin/eval-pom_ just provides a small helper to derive Maven 
POM parameters into the current environment.