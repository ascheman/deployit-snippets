import os
import sys

def trace(msg):
    if os.environ.has_key("DEPLOYIT_CLI_LOGLEVEL") and os.environ["DEPLOYIT_CLI_LOGLEVEL"] >= 9:
        print >> sys.stderr, msg
        
