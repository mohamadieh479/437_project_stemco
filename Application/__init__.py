from flask import Flask

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='dev')
from DataBaseTools.creatingDB import init_db_command
app.cli.add_command(init_db_command)

from Application import routes

from Application import test_routes #This file is only for testing and should be removed by end of project