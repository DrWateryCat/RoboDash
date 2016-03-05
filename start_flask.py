import flask

from os.path import abspath, dirname, exists, join
from optparse import OptionParser

from networktables import NetworkTable
from pynetworktables2js import get_handlers, NonCachingStaticFileHandler

import logging
logger = logging.getLogger('dashboard')

log_datefmt = "%H:%M:%S"
log_format = "%(asctime)s:%(msecs)03d %(levelname)-8s: %(name)-20s: %(message)s"

def init_networktables(ipaddr):

    logger.info("Connecting to networktables at %s" % ipaddr)
    NetworkTable.setIPAddress(ipaddr)
    NetworkTable.setClientMode()
    NetworkTable.initialize()
    logger.info("Networktables Initialized")
    
app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.url_for('www', filename='index.html')    

if __name__ == "__main__":
    app.run()