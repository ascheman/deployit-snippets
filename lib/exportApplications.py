import sys
import re
import os

import getopt

from tools import *

def usage(progName, exitCode, message = None):
    usage = "usage: " + progName + " -h | [ -f ] [ -n ] [ -t targetDir ] { -a includePattern [ -x excludePattern ] | [ -p ] application+ }"
    if message:
    	print >> sys.stderr, message
    if exitCode > 0:
    	print >> sys.stderr, usage
    else:
        print (usage) 
    sys.exit(exitCode)
    	
def main(argv):    	
    opts, args = getopt.getopt(sys.argv[1:], "ha:fnpt:x:")
    # List version numbers (long listing) also
    targetDir = ""
    forceOverwrite = 0
    dryRun = 0
    preservePath = 0
    includePattern = None
    excludePattern = None
    for opt, arg in opts:
    	if opt == "-h":
    	    usage(argv[0], 0)
        elif opt == "-a":
            includePattern = arg
        elif opt == "-f":
            forceOverwrite = 1
        elif opt == "-n":
            dryRun = 1
        elif opt == "-p":
            preservePath = 1
        elif opt == "-t":
            targetDir = arg
        elif opt == "-x":
            excludePattern = arg
    
    applications = args
    if includePattern:
    	if len(args) != 0:
    	    usage(argv[0], 1, "Option '-a' and a list of applications is mutually exclusive")
    	elif preservePath:
    	    usage(argv[0], 1, "Options '-a' and '-p' are mutually exclusive")
    	    
    	preservePath = 1
        applications = listApplications (repository, 1, includePattern, excludePattern)
    elif excludePattern:
    	usage(argv[0], 1, "Option '-x' must not be used without '-a'")
    elif len(args) == 0:
    	usage(argv[0], 1, "Please specify either one or more application(s) or a search pattern with '-a'")
    	
    for application in applications:
    	trace ("Exporting '%s'" % application)
    	exportApplication(repository, application, targetDir, forceOverwrite, dryRun, preservePath)
    	      
# The usual way to start main does not work, obviously the script is embedded somehow?
# if __name__ == "__main__":
trace ("Calling main(" + str(sys.argv) + ")")
main(sys.argv)