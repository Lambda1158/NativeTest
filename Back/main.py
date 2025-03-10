from flask import Flask
import requests
app=Flask(__name__)

CLIENT_ID="87e6f8eaf85f4a748af9402e75029d42"
CLIENT_SECRET="d6a26aded67d49f5ac6174360cff4254"
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
	