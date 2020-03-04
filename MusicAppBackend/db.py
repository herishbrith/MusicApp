"""
Author: Harsh Bhardwaj
Project: MusicApp
Date: 4th Mar 2020
"""

"""
Database configuration file
"""


# Import packages
from flaskext.mysql import MySQL
from config import Config


class MySQL_DB:
	"""
		Database connector
	"""

	# DB handler
	db = MySQL()

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

		# Initiate DB app
		MySQL_DB.db.init_app(app)


	@staticmethod
	def set_connection():
		"""
			If connection is not found or is inactive, re-connect
		"""
		if not (MySQL_DB.conn and MySQL_DB.conn.open):
			try:
				# initiate DB connection
				MySQL_DB.conn = MySQL_DB.db.connect()
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




