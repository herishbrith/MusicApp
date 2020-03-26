"""
Author: Harsh Bhardwaj
Project: MusicApp
Date: 4th Mar 2020
"""

"""
Database configuration file
"""


# Import packages
import sqlite3
from config import Config


class MySQL_DB:
	"""
		Database connector
	"""

	# DB connection
	conn = None

	@staticmethod
	def initiate_app(app):
		"""
			Setup app configurations
		"""

		# add database configurations to app
		app.config["MYSQL_DATABASE_USER"] = Config.MYSQL_DATABASE_USER
		app.config["MYSQL_DATABASE_PASSWORD"] = Config.MYSQL_DATABASE_PASSWORD
		app.config["MYSQL_DATABASE_DB"] = Config.MYSQL_DATABASE_DB
		app.config["MYSQL_DATABASE_HOST"] = Config.MYSQL_DATABASE_HOST


	@staticmethod
	def set_connection():
		try:
			# initiate DB connection
			MySQL_DB.conn = sqlite3.connect("database.db")
		except Exception as excp:
			raise excp


	@staticmethod
	def close_connection():
		"""
			Close db connection
		"""
		if MySQL_DB.conn and MySQL_DB.conn.open:
			MySQL_DB.conn.close()


	@staticmethod
	def query(query, commit=False):
		"""
			:params:
				query: SQL query
				commit: whether or not to commit the query
			:returns: DB cursor to fetch data from
		"""
		try:
			MySQL_DB.set_connection()
			cursor = MySQL_DB.conn.cursor()
			cursor.execute(query)

			if commit:
				MySQL_DB.conn.commit()
			return cursor
		except Exception as excp:
			raise excp




