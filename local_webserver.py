#!/usr/bin/env python3

"""
This module launches a simple web server using the files stored on your PC.
This lets you preview the result of any changes without pushing them to GitHub.
"""

import http.server
import sys

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):

    """
    Disable caching.
    
    Without this the browser might store a cached version of a file (e.g. an image or
    a CSS stylesheet) and keep serving the old version even after the original file has
    been modified on disk.
    """
    def send_response_only(self, code, message=None):
        super().send_response_only(code, message)
        self.send_header('Cache-Control', 'max-age=0, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', 'Wed, 11 Jan 1984 05:00:00 GMT')

if __name__ == '__main__':
    
    port = 8000
    if len(sys.argv) > 1:
        port = sys.argv[1]
    
    http.server.test(HandlerClass=NoCacheHTTPRequestHandler, port=port)
