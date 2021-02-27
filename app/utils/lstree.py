from . import ls
import sys
import os

def lstree(path):
    output=[]
    scan=[path]
    while len(scan):
        for item in ls(scan.pop(0)):
            if os.path.isdir(item):
                scan.append(item)
            else:
                output.append(item)
    return output

sys.modules[__name__] = lstree
