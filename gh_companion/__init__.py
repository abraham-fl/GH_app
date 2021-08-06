from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config["SECRET_KEY"] = "b30e0c86b3e25d58c33d122fac503adf"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db" #/// = rel. path

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login" #route die aufgerufen wird, wenn ein nicht eingeloggter User versucht, eine nicht erlaubte Seite zu öffnen
login_manager.login_message_category = "info" #"info" == bootstrap info class

from gh_companion import routes