from flask import Flask

app = Flask(__name__)

from Application import routes

from Application import test_routes #This file is only for testing and should be removed by end of project