from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from gh_companion.config import Config

#Extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "users.login" #route die aufgerufen wird, wenn ein nicht eingeloggter User versucht, eine nicht erlaubte Seite zu öffnen
login_manager.login_message_category = "info" #"info" == bootstrap info class

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from gh_companion.users.routes import users 
    from gh_companion.characters.routes import characters 
    from gh_companion.main.routes import main 

    app.register_blueprint(users)
    app.register_blueprint(characters)
    app.register_blueprint(main)

    return app

