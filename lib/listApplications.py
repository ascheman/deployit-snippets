import sys
import os

import getopt

from tools import *

def usage(progName, exitCode):
    print "usage: " + progName + " -h | [-l] [-x excludeRegex] [includeRegex]"
    sys.exit(exitCode)
    	
def main(argv):    	
    opts, args = getopt.getopt(sys.argv[1:], "hlx:")
    # List version numbers (long listing) also
    listLong = 0
    excludePattern = None
    for opt, arg in opts:
    	if opt == "-h":
    	    usage(argv[0], 0)
        elif opt == "-l":
            listLong = 1
        elif opt == "-x":
            excludePattern = arg

    searchPattern = "Applications/"
    if len(args) == 1:
        searchPattern = args[0]
    elif len(args) > 1:
        usage(argv[0], 1)

    appNames = listApplications (repository, listLong, searchPattern, excludePattern)
    	
    for appName in appNames:
        print appName
        
# The usual way to start main does not work, obviously the script is embedded somehow?
# if __name__ == "__main__":
trace ("Calling main(" + str(sys.argv) + ")")
main(sys.argv)