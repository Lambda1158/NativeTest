# app/routes/spotify.py
from flask import Blueprint, jsonify, session, url_for, redirect
import requests
from config import Config
from app import cache
from app.lib.middleware import token_required
from app import sp
spotify_bp = Blueprint('spotify', __name__)

@spotify_bp.route("/top-tracks")
@cache.cached(timeout=300)
@token_required
def get_top_tracks():
    headers = {
        "Authorization": f"Bearer {session['access_token']}"
    }
    params = {
        "time_range": "short_term",  # Últimas 4 semanas
        "limit": 15  # Número de tracks a obtener
    }
    top_tracks_response = requests.get(Config.API_BASE_URL + "me/top/tracks", headers=headers, params=params)
    top_tracks = top_tracks_response.json()

    return jsonify(top_tracks)

@spotify_bp.route("/playlist")
@token_required
def get_playlist():
    playlists = sp.current_user_playlists()
    return jsonify(playlists)
    
@spotify_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.home"))

