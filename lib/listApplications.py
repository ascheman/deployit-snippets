import sys
import re
import os

def trace(msg):
    if os.environ.has_key("DEPLOYIT_CLI_LOGLEVEL") and os.environ["DEPLOYIT_CLI_LOGLEVEL"] >= 9:
    	print >> sys.stderr, msg

searchPattern = "Applications/"
if len(sys.argv) > 1:
    searchPattern = sys.argv[1]
trace ("Searching by Pattern '" + searchPattern + "'")

pathes=repository.search('udm.DeploymentPackage')

apps = dict()
for path in pathes:
    dirname = os.path.dirname(path)
    trace ("Found '" + dirname + "'")
    if re.search (searchPattern, dirname):
    	if apps.has_key(dirname):
    	    apps[dirname] += 1
    	else:
    	    apps[dirname] = 0
    	
for appName in sorted(apps.keys()):
    print appName