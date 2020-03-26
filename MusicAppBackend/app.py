"""
Author: Harsh Bhardwaj
Project: MusicApp
Date: 4th Mar 2020
"""

"""
Configures and runs the server app
"""


# Import libraries
import os
import json

from flask import Flask

from app import controllers as AppControllers
from config import Config
from db import MySQL_DB


# Create app and register URLs
app = Flask(__name__, template_folder="templates")
app.register_blueprint(
	AppControllers.controller,
	url_prefix="/"
)

# Initiate DB connection
MySQL_DB.initiate_app(app)
MySQL_DB.set_connection()

# Configure the app and start running
if __name__ == "__main__":
	app.run(
		debug=Config.DEBUG,
		host=Config.HOST,
		port=Config.PORT
	)

	Config.PROJECT_DIR = app.instance_path




