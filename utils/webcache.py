from . import lstree
import sys

def webcache(path):
    ltnSc = len(path)
    output = { 'uri': [], 'cache': [] }
    for path in lstree(path):
        # Load
        uri = path[ltnSc:]
        with open(path) as f:
            data = f.read()
        # Add
        output['uri'].append(uri)
        output['cache'].append({
            'path': path,
            'data': data
        })
    return output

sys.modules[__name__] = webcache
