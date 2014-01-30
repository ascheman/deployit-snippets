import sys
import re
import os

import getopt

from tools import trace

def usage(progName, exitCode):
    print "usage: " + progName + " -h | [-l] [searchRegex]"
    sys.exit(exitCode)
    	
def main(argv):    	
    opts, args = getopt.getopt(sys.argv[1:], "hl")
    # List version numbers (long listing) also
    listLong = 0
    for opt, arg in opts:
    	if opt == "-h":
    	    usage(argv[0], 0)
        elif opt == "-l":
            listLong = 1

    searchPattern = "Applications/"
    if len(args) == 1:
        searchPattern = args[0]
    elif len(args) > 1:
        usage(argv[0], 1)
        
    trace ("Searching by Pattern '" + searchPattern + "'")

    pathes=repository.search('udm.DeploymentPackage')
    
    apps = dict()
    for path in pathes:
        if listLong:
            name = path
        else:
            name = os.path.dirname(path)
        trace ("Found '" + name + "'")
        if re.search (searchPattern, name):
        	if apps.has_key(name):
        	    apps[name] += 1
        	else:
        	    apps[name] = 0
    	
    for appName in sorted(apps.keys()):
        print appName
        
# if __name__ == "__main__":
trace ("Calling main(" + str(sys.argv) + ")")
main(sys.argv)