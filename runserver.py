"""
This script runs the SBFXPROTOCOL application using a development server.
"""

from os import environ
from SBFXPROTOCOL import app
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple






if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
