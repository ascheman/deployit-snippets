import sys
import re
import os

import getopt

### TODO it is somehow not possible to import the thrown Java exception to perform a proper error handling!

# import com.xebialabs.deployit.service.importer.ImporterException
# sys.add_package('com.xebialabs.deployit.service.importer')
# from com.xebialabs.deployit.service.importer import ImporterException
# import ImporterException

from tools import trace

def usage(progName, exitCode, message = None):
    usage = "usage: " + progName + " -h | [ -n ] darfile+"
    if message:
        print >> sys.stderr, message
    if exitCode > 0:
        print >> sys.stderr, usage
    else:
        print (usage) 
    sys.exit(exitCode)
    	
def main(argv):    	
    opts, args = getopt.getopt(argv[1:], "hn")
    dryRun = 0
    for opt, arg in opts:
    	if opt == "-h":
    	    usage(argv[0], 0)
    	elif opt == "-n":
    	    dryRun = 1
       
    if len(args) < 1:
        usage(argv[0], 1)

    for applicationFile in args:
    	if not os.path.exists(applicationFile):
    	    print >> sys.stderr, "Application file '%s' does not exists!" % applicationFile
    	    continue
    	applicationName = applicationFile[0:-4]
        filePath = os.path.join (os.path.realpath("."), applicationFile) 
    	importMsg = "Importing application '%s' from file '%s'" % (applicationName, filePath)
    	if repository.exists(applicationName):
    	    print ("Application '%s' already exists - skipped" % applicationName)
    	elif dryRun:
    	    print (importMsg + " - skipped (DryRun!)")
    	else:
            print (importMsg)
            try:
                deployit.importPackage(filePath)
# Check out the TODO in the import section!
#            except ImporterException, e:
#                print >> sys.stderr, "Could not import DAR from '%s': '%s'" % (applicationFile, e.strerror)
            except:
                print >> sys.stderr, "Could not import DAR from '%s'!" % (applicationFile)
        
# The usual way to start main does not work, obviously the script is embedded somehow?
# if __name__ == "__main__":
trace ("Calling main(" + str(sys.argv) + ")")
main(sys.argv)