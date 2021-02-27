#!/bin/python3
import subprocess
import sys

def ls(path):
    out = subprocess.check_output(('ls ' + path).split(' ')).decode('utf-8')
    return [('%s/%s' % (path, x)) for x in out.split('\n')[:-1]]

sys.modules[__name__] = ls
