from flask import Flask, session
from config import Config
from flask_caching import Cache
from spotipy import Spotify 
from spotipy.oauth2 import SpotifyOAuth 
from spotipy.cache_handler import FlaskSessionCacheHandler  


scope = "user-read-private user-read-email user-top-read user-read-recently-played"
params = {
    "client_id": Config.CLIENT_ID,
    "response_type": "code",
    "scope": scope,
    "redirect_uri": Config.REDIRECT_URI,
    "show_dialog": True
}
cache_handler = FlaskSessionCacheHandler(session=session)
sp_oauth = SpotifyOAuth(client_id=Config.CLIENT_ID,client_secret=Config.CLIENT_SECRET,scope=scope,redirect_uri=Config.REDIRECT_URI,cache_handler=cache_handler)
sp = Spotify(auth_manager=sp_oauth)

cache = Cache()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    app.config["CACHE_TYPE"] = "SimpleCache"
    app.config["CACHE_DEFAULT_TIMEOUT"] = 300
    cache.init_app(app)
    
    # Registra los blueprints (rutas)
    from app.routes.auth import auth_bp
    from app.routes.spotify import spotify_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(spotify_bp)

    return app

