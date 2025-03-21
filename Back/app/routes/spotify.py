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
	top_tracks = sp.current_user_top_tracks(limit=5)
	return jsonify(top_tracks)

@spotify_bp.route("/playlist")
@token_required
def get_playlist():
    playlists = sp.current_user_playlists(limit=5, offset=0)
    return jsonify(playlists)
    
@spotify_bp.route("/recently-played")
@token_required
def get_user_recently_played():
      recently_played = sp.current_user_recently_played(limit=10, after=None, before=None)
      return jsonify(recently_played)

@spotify_bp.route("/top-artists")
@token_required
def get_user_top_artists():
      top_artists = sp.current_user_top_artists(limit=5)
      return jsonify(top_artists)

@spotify_bp.route("/user-info")
@token_required
def get_user():
      user_info = sp.current_user()
      return jsonify(user_info)