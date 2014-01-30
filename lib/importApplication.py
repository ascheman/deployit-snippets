import sys
import re
import os

import getopt

from tools import trace

def usage(progName, exitCode):
    print "usage: " + progName + " -h | darfile"
    sys.exit(exitCode)
    	
def main(argv):    	
    opts, args = getopt.getopt(sys.argv[1:], "h")
    # List version numbers (long listing) also
    for opt, arg in opts:
    	if opt == "-h":
    	    usage(argv[0], 0)
       
    if len(args) != 1:
        usage(argv[0], 1)
    application = args[0]

    filePath = os.path.join (os.path.realpath("."), application) 
    trace ("Importing application '%s' from file '%s'" % (application, filePath))
    deployit.importPackage(filePath)
        
# The usual way to start main does not work, obviously the script is embedded somehow?
# if __name__ == "__main__":
trace ("Calling main(" + str(sys.argv) + ")")
main(sys.argv)