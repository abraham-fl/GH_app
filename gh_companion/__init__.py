from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from gh_companion.config import Config
app = Flask(__name__)


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login" #route die aufgerufen wird, wenn ein nicht eingeloggter User versucht, eine nicht erlaubte Seite zu öffnen
login_manager.login_message_category = "info" #"info" == bootstrap info class

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from gh_companion import routes
    
    return app

