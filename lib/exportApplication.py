import sys
import re
import os

import getopt

from tools import trace

def usage(progName, exitCode):
    print "usage: " + progName + " -h | [ -t targetDir ] [ -p ] application"
    sys.exit(exitCode)
    	
def main(argv):    	
    opts, args = getopt.getopt(sys.argv[1:], "hpt:")
    # List version numbers (long listing) also
    targetDir = ""
    preservePath = 0
    for opt, arg in opts:
    	if opt == "-h":
    	    usage(argv[0], 0)
        elif opt == "-t":
            targetDir = arg
        elif opt == "-p":
            preservePath = 1
       
    if len(args) != 1:
        usage(argv[0], 1)
    application = args[0]

    if targetDir != "":
    	if targetDir[-1] != "/" and targetDir[-1] != os.pathsep:
    	    trace ("Prepending path separator to target path")
            targetDir += "/"
    else:
        trace ("Using current dir as target dir") 
        targetDir = "./"
    if preservePath:
    	targetDir += os.path.dirname (application)
    trace ("Exporting application '" + application + "' to target directory '" + targetDir + "'")
    pathes=repository.exportDar(targetDir, application)
    if preservePath:
        # Fix the exportDar output name, eg. 
        #   it is dumped as Applications/xxx/yyy/<appName>/<appName>-<appVersion>.dar
        #   but the name should be Applications/xxx/yyy/<appName>/<appVersion>.dar
    	appVersion = os.path.basename(application)
    	dirName = os.path.dirname(application)
    	appName = os.path.basename(dirName)
    	darName = appName + "-" + appVersion + ".dar"
    	# This is the current path of the dar file
    	darSourcePath = dirName + "/" + darName
    	# This is the final target path of the dar file
    	darTargetPath = dirName + "/" + appVersion + ".dar"
    	trace ("Fixing the dar name from '%s' to '%s'" % (darSourcePath, darTargetPath))
        os.rename (darSourcePath, darTargetPath)
        
# The usual way to start main does not work, obviously the script is embedded somehow?
# if __name__ == "__main__":
trace ("Calling main(" + str(sys.argv) + ")")
main(sys.argv)