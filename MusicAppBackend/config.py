"""
Author: Harsh Bhardwaj
Project: MusicApp
Date: 4th Mar 2020
"""

"""
Database configuration file
"""


class Config:
	"""
		Production configurations
	"""

	# app config variables
	DEBUG = False
	HOST = "0.0.0.0"
	PORT = 8000
	DROP_INTRUDER_REQUESTS = True

	# DB credentials
	MYSQL_DATABASE_USER = ""
	MYSQL_DATABASE_PASSWORD = ""
	MYSQL_DATABASE_DB = ""
	MYSQL_DATABASE_HOST = ""




