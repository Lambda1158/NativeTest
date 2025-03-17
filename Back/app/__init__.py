# app/__init__.py
from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Registra los blueprints (rutas)
    from app.routes.auth import auth_bp
    from app.routes.spotify import spotify_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(spotify_bp)

    return app

