import os
import re
import sys

def trace(msg):
    if os.environ.has_key("DEPLOYIT_CLI_LOGLEVEL") and os.environ["DEPLOYIT_CLI_LOGLEVEL"] >= 9:
        print >> sys.stderr, msg
        
        
def listApplications(repository, listLong = 0, searchPattern = None, excludePattern = None):
    pathes=repository.search('udm.DeploymentPackage')
    
    trace ("Including pathes with pattern '%s', excluding '%s'" % (searchPattern, excludePattern))
    # Exclude unwanted pathes
    if excludePattern:
    	filteredPathes = []
    	for path in pathes:
            trace ("Checking '%s' for exclusion" % path)
    	    if not re.search (excludePattern, path):
    	    	filteredPathes.append(path)
    	pathes = filteredPathes

    # Include wanted pathes	    	
    if searchPattern:
        filteredPathes = []
        for path in pathes:
            trace ("Checking '%s' for inclusion" % path)
            if re.search (searchPattern, path):
            	filteredPathes.append(path)
        pathes = filteredPathes
            	
    if not listLong:
        apps = dict()
    	for path in pathes:
    	    shortName = os.path.dirname(path)
            if apps.has_key(shortName):
                apps[shortName] += 1
            else:
                apps[shortName] = 0
        pathes = apps.keys()
            
    return sorted(pathes)
