from flask import Flask
from dotenv import load_dotenv
import os
import requests
app=Flask(__name__)

CLIENT_ID=os.getenv('CLIENT_ID')
CLIENT_SECRET=os.getenv('CLIENT_SECRET')
REDIRECT_URI="http://localhost:5000/callback"
AUTH_URL="https://accounts.spotify.com/authorize"
TOKEN_URL="https://accounts.spotify.com/authorize/api/token"
API_BASE_URL="https://api.spotify.com/v1/"


@app.route("/")
def index():
	return "welcome to my spotify web app"

@app.route("/login")
def login():
	scope="user-read-private user-read-email"
	params={"client_id":CLIENT_ID,
		 "response_type":"code",
		 "scope":scope,
		 "redirect_uri":REDIRECT_URI,
		 "show_dialog":True}
	