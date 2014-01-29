import sys
import re

searchPattern = "Applications/"
if len(sys.argv) > 1:
    searchPattern = sys.argv[1]

print "Searching by Pattern '" + searchPattern + "'"
apps=repository.search('udm.DeploymentPackage')
for app in apps:
    if re.search (searchPattern, app):
        print app