from flask import Flask

from random import randrange
import xarray as xr
import sys


server = Flask(__name__)

@server.route('/random')
def hello():
    return str(randrange(100))

@server.route('/xarray')
def xarray():
    xr.show_versions()
    modulename = 'xarray'
    if modulename not in sys.modules:
        return str("xarray not in sys.modules")
    else:
        return str("xarray was imported")

@server.route('/helloworld')
def helloworld():
    return str("Hello World")


if __name__ == "__main__":
   server.run(host='0.0.0.0')