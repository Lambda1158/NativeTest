# app/routes/auth.py
from flask import Blueprint, redirect, request, session, url_for, jsonify
import requests
from datetime import datetime
from config import Config
from app.lib.middleware import token_required
from app import sp_oauth,cache_handler,params

auth_bp = Blueprint('auth', __name__)


@auth_bp.route("/")
@token_required
def home():
    return redirect(url_for('spotify.get_playlist'))


@auth_bp.route("/login")
def login():
    auth_url = f"{Config.AUTH_URL}?{'&'.join([f'{key}={value}' for key, value in params.items()])}"
    return redirect(auth_url)

@auth_bp.route("/callback")
def callback():
    sp_oauth.get_access_token(request.args["code"])
    
    return redirect(url_for("spotify.get_playlist"))