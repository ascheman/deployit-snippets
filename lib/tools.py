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
    
def exportApplication(repository, application, targetDir = None, forceOverwrite = 0, dryRun = 0, preservePath = 0):
    trace ("Exporting application '%s' to target directory '%s' (overwrite = %d, dryRun = %d, preservePath = %d)" % (application, targetDir, forceOverwrite, dryRun, preservePath))
    if targetDir and targetDir != "":
        if targetDir[-1] != "/" and targetDir[-1] != os.pathsep:
            trace ("Prepending path separator to target path")
            targetDir += "/"
    else:
        trace ("Using current dir as target dir") 
        targetDir = "./"
        
    # Calculate the DAR file output name, eg. 
    #   it is dumped as Applications/xxx/yyy/<appName>/<appName>-<appVersion>.dar
    #   but the name should be Applications/xxx/yyy/<appName>/<appVersion>.dar
    appVersion = os.path.basename(application)
    dirName = os.path.dirname(application)
    appName = os.path.basename(dirName)
    darName = appName + "-" + appVersion + ".dar"
    if preservePath:
        targetDir += os.path.dirname (application) + "/"
        # This is the current path of the dar file
        darSourcePath = targetDir + darName
        # This is the final target path of the dar file
        darTargetPath = targetDir + appVersion + ".dar"
        trace ("Fixing the dar name from '%s' to '%s'" % (darSourcePath, darTargetPath))
    else:
        darTargetPath = targetDir + darName

    if os.path.exists(darTargetPath):
    	msg = "Target DAR '%s' already exists" % darTargetPath
    	if forceOverwrite:
    	    if dryRun:
    	    	print (msg + " - NOT overwriting it (DryRun)")
    	    	return
    	    else:   	    
    	        print (msg + " - overwriting it (FORCED!)")
    	        os.remove (darTargetPath)
    	else:
    	    print (msg + " - NOT overwriting it!")
            return
    	        
    repository.exportDar(targetDir, application)
    if preservePath:
        os.rename (darSourcePath, darTargetPath)

