from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Importa blueprint
from app.routes.client_route import client_router

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(client_router)
    db = SQLAlchemy(app)
    return app