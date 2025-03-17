from flask import Flask, redirect, request, jsonify, session
from dotenv import load_dotenv
from datetime import datetime,timedelta
import os
import requests

load_dotenv()

app=Flask(__name__)

CLIENT_ID=os.getenv('CLIENT_ID')
CLIENT_SECRET=os.getenv('CLIENT_SECRET')
REDIRECT_URI="http://localhost:5000/callback"
AUTH_URL="https://accounts.spotify.com/authorize"
TOKEN_URL="https://accounts.spotify.com/api/token"
API_BASE_URL="https://api.spotify.com/v1/"


@app.route("/")
def index():
	return "welcome to my spotify web app"

@app.route("/login")
def login():
	scope = "user-read-private user-read-email"
	params = {"client_id":CLIENT_ID,
		 "response_type":"code",
		 "scope":scope,
		 "redirect_uri":REDIRECT_URI,
		 "show_dialog":True}
	auth_url = f"{AUTH_URL}?{'&'.join([f'{key}={value}' for key, value in params.items()])}"
	return redirect(auth_url)

@app.route("/callback")
def callback():
	if "error" in request.args:
		return jsonify({"error":request["error"]})
	if "code" in request.args:
		req_body ={
			"code":request["code"],
			"grant_type":"authorization_code",
			"redirect_uri":REDIRECT_URI,
			"client_id":CLIENT_ID,
			"client_secret":CLIENT_SECRET,
		}
		response = request.post(TOKEN_URL,data=req_body)
		token_info = response.json()
		session["access_token"] = token_info["access_token"]
		session["refresh_token"] = token_info["refresh_token"]
		session["expires_at"] = datetime.now().timestamp() + token_info["expires_in"]
		return redirect("/playlist")

@app.route("/playlist")
def get_playlist():
	if "access_token" not in session:
		return redirect("/login")
	if datetime.now().timestamp() > session["expires_at"]:
		return redirect("/refresh-token")
	headers = {
		"Authorization": f"Bearer {session["access_token"]}"
	}


