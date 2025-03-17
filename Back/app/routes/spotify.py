# app/routes/spotify.py
from flask import Blueprint, jsonify, redirect, session, url_for
import requests
from datetime import datetime
from config import Config

spotify_bp = Blueprint('spotify', __name__)

@spotify_bp.route("/top-tracks")
def get_top_tracks():
    if "access_token" not in session:
        return redirect(url_for("auth.login"))
    if datetime.now().timestamp() > session["expires_at"]:
        return redirect(url_for("auth.refresh_token"))

    headers = {
        "Authorization": f"Bearer {session['access_token']}"
    }

    params = {
        "time_range": "short_term",  # Últimas 4 semanas
        "limit": 10  # Número de tracks a obtener
    }
    top_tracks_response = requests.get(Config.API_BASE_URL + "me/top/tracks", headers=headers, params=params)
    top_tracks = top_tracks_response.json()

    return jsonify(top_tracks)

@spotify_bp.route("/playlist")
def get_playlist():
	if "access_token" not in session:
		return redirect("/login")
	if datetime.now().timestamp() > session["expires_at"]:
		return redirect("/refresh-token")
	headers = {
		"Authorization": f"Bearer {session["access_token"]}"
	}
	response = requests.get(Config.API_BASE_URL + "me/playlists", headers=headers)
	playlist = response.json()
	return jsonify(playlist)


@spotify_bp.route("/")
def index():
	url_redirect = url_for("auth.login")
	return  f'''
    <h1 style="color: blue; text-align: center;">¡Bienvenido a mi aplicación!</h1>
    <p style="text-align: center;">Este es un texto con un adorno.</p>
    <p style="text-align: center;">
        <a href="{url_redirect}" style="color: green; text-decoration: none;">
            Llevame al login
        </a>
    </p>
    '''