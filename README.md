deployit-snippets
=================

This project contains some snippets for XebiaLabs DeployIt, e.g., command line and jython scripts.

Improved command line script
----------------------------

The default DeployIt CLI (shell) startup script has two drawbacks:
- On cygwin based environments it did not properly call Java: The JAR pathes need to be Windows path names (i.e. with Drive letter etc.), separated by ';' instead of ':'
- It performs a "cd" (Change Directory) command internally and therefor cannot handle relative paths, for, e.g., Jython scripts which should be executed on the server side.

The version in "bin/deployit-cli.sh" circumvents these two problems.

Additionally the extended cli tries to read a $HOME/.deployitrc. It works like a Windows INI file, i.e., it is divided into sections for different DeployIt environments, each starting with a '[$environment]' line.
The file is configured via the DEPLOYIT_CLI_RC environment variable. 
Make sure it has some lists of the form

 [xxx]
 username abc
 password def
 server ghi
 ...
 [yyy]
 ...

with name/value parameters for each environment!
The particular environment is select from the DEPLOYIT_CLI_ENV environment variable.

Eval-POM
---------

The script _bin/eval-pom_ just provides a small helper to derive Maven 
POM parameters into the current environment.