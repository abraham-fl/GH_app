from gh_companion import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)

    characters = db.relationship("Character", backref="Owner", lazy=True)

    def __repr__(self):
        return f"{self.username}"


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classname = db.Column(db.String(50), unique=True, nullable=False)
    character_image = db.Column(
        db.String(20), nullable=False, default="default_char.jpg"
    )
    given_name = db.Column(db.String(50), nullable=False)
    lvl = db.Column(db.Integer, nullable=False, default=1)
    exp = db.Column(db.Integer, nullable=False, default=0)
    items = db.Column(db.String(9001))
    retired = db.Column(db.Boolean, default=False, nullable=False)
    max_life = db.Column(db.Integer, nullable=False, default=0)
    current_life = db.Column(db.Integer, nullable=False, default=0)
    hand_size = db.Column(db.Integer, nullable=False, default=0)

    perks = db.relationship("Perk", backref="Owner", lazy=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"{self.given_name}\n Level {self.lvl} {self.classname}"


class Perk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250), nullable=False)
    max_level = db.Column(db.Integer, nullable=False, default=1)
    current_level = db.Column(db.Integer, nullable=False, default=0)
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"), nullable=False)
