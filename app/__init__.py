from flask import Flask
from app.config import Config
from app.api.users import users_bp
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) 
    
    app.register_blueprint(users_bp)
    
    return app
