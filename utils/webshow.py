import mimetypes
import sys

# Use with webcache
def webshow(wcache, uri):
    # Errors
    status = 200
    msg_error = 404, None, None
    if not len(uri): return msg_error
    if uri[-1] == '/': uri += 'index.html'
    if not uri in wcache['uri']:
        status = 404
        uri = '/error404.html'
        if not uri in wcache['uri']: return msg_error
    # Found
    data = wcache['cache'][wcache['uri'].index(uri)]['data']
    return status, mimetypes.guess_type(uri)[0], data

sys.modules[__name__] = webshow
