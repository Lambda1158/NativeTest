# app/routes/auth.py
from flask import Blueprint, redirect, request, session, url_for, jsonify
import requests
from datetime import datetime
from config import Config

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login")
def login():
    scope = "user-read-private user-read-email user-top-read"
    params = {
        "client_id": Config.CLIENT_ID,
        "response_type": "code",
        "scope": scope,
        "redirect_uri": Config.REDIRECT_URI,
        "show_dialog": True
    }
    auth_url = f"{Config.AUTH_URL}?{'&'.join([f'{key}={value}' for key, value in params.items()])}"
    return redirect(auth_url)

@auth_bp.route("/callback")
def callback():
    if "error" in request.args:
        return jsonify({"error": request.args["error"]})
    if "code" in request.args:
        req_body = {
            "code": request.args["code"],
            "grant_type": "authorization_code",
            "redirect_uri": Config.REDIRECT_URI,
            "client_id": Config.CLIENT_ID,
            "client_secret": Config.CLIENT_SECRET,
        }
        response = requests.post(Config.TOKEN_URL, data=req_body)
        token_info = response.json()
        session["access_token"] = token_info["access_token"]
        session["refresh_token"] = token_info["refresh_token"]
        session["expires_at"] = datetime.now().timestamp() + token_info["expires_in"]
        return redirect(url_for("spotify.get_top_tracks"))