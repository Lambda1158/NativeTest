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
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to My Spotify Expo App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #1DB954;
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                text-align: center;
            }
            h1 {
                font-size: 3rem;
                margin-bottom: 20px;
            }
            p {
                font-size: 1.2rem;
            }
            .btn {
                background-color: #191414;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                font-size: 1rem;
                cursor: pointer;
                margin-top: 20px;
            }
            .btn:hover {
                background-color: #333;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to My Spotify Expo App</h1>
            <p>Explore your favorite music and playlists with ease.</p>
            <button class="btn" onclick="window.location.href='/login'">Login with Spotify</button>
        </div>
    </body>
    </html>
    '''


@auth_bp.route("/login")
def login():
    auth_url = f"{Config.AUTH_URL}?{'&'.join([f'{key}={value}' for key, value in params.items()])}"
    return redirect(auth_url)

@auth_bp.route("/callback")
def callback():
    sp_oauth.get_access_token(request.args["code"])
    return redirect(url_for("auth.home"))

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.home"))