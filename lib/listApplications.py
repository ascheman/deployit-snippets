import sys
import re
import os

import getopt

def trace(msg):
    if os.environ.has_key("DEPLOYIT_CLI_LOGLEVEL") and os.environ["DEPLOYIT_CLI_LOGLEVEL"] >= 9:
    	print >> sys.stderr, msg
    	
    	
def main(argv):    	
    opts, args = getopt.getopt(sys.argv[1:], "l")
    # List version numbers (long listing) also
    listLong = 0
    for opt, arg in opts:
        if opt == "-l":
            listLong = 1

    searchPattern = "Applications/"
    if len(args) > 1:
        searchPattern = sys.argv[1]
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