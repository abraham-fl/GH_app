from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "b30e0c86b3e25d58c33d122fac503adf"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db" #/// = rel. path

db = SQLAlchemy(app)

from gh_companion import routes