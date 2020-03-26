"""
Author: Harsh Bhardwaj
Project: MusicApp
Date: 4th Mar 2020
"""

"""
Module for handling incoming requests to server
"""


from flask import Blueprint, render_template, request
from flask import redirect, jsonify
controller = Blueprint("main", __name__)

from db import MySQL_DB


def process_post_data(stringData):
	return {
		pair.split("=")[0]: pair.split("=")[1] \
		for pair in \
		str(stringData).replace("b'", "").replace("'", "").split("&")
	}


def get_one_song(songId):
	resCursor = MySQL_DB.query(
		"SELECT * FROM songs WHERE id=%s" % (songId)
	)
	return resCursor.fetchone()


def get_all_songs():
	resCursor = MySQL_DB.query(
		"SELECT * FROM songs"
	)
	rows = resCursor.fetchall()
	return rows


def save_new_song(formData):
	saveQuery = """
		INSERT INTO songs (title, artist, album)
		VALUES ('%s', '%s', '%s')
	""" % (
		formData["title"],
		formData["artist"],
		formData["album"]
	)

	try:
		resCursor = MySQL_DB.query(saveQuery, commit=True)
		return True
	except Exception as excp:
		return False


def delete_one_song(songId):
	try:
		resCursor = MySQL_DB.query(
			"DELETE FROM songs WHERE id=%s" % (songId),
			commit=True
		)
	except Exception as excp:
		return False


@controller.route("/", methods=["GET", "POST"])
def get_home_page():
	rows = get_all_songs()
	return render_template("index.html", rows=rows)


@controller.route("/song", methods=["GET", "POST", "DELETE"])
def create_song():
	if request.method == "GET":
		return render_template("song.html")
	elif request.method == "POST":
		if not (request.form["title"] and \
			request.form["artist"] and \
			request.form["album"]
		):
			saved = False
		else:
			saved = save_new_song(request.form)
		return render_template("song.html", saved=saved)
	elif request.method == "DELETE":
		data = process_post_data(request.data)
		result = delete_one_song(data["id"])
		if result:
			response = {
				"status": 200
			}
		else:
			response = {
				"status": 500
			}
		return render_template("index.html")


@controller.route("/view/<int:songId>", methods=["GET", "DELETE"])
def view_song(songId):
	if request.method == "GET":
		data = get_one_song(songId)
		return render_template("view.html", data=data)
	elif request.method == "DELETE":
		print(request.form)
		return render_template("song.html", saved=saved)

	


