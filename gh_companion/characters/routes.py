from flask import Blueprint
from flask import render_template
from gh_companion.models import Character
from flask_login import login_required

characters = Blueprint("characters", __name__)

@characters.route("/character/<int:char_id>")
@login_required
def character(char_id):
    character = Character.query.get_or_404(char_id)
    return render_template("character.html", title="Character Sheet", character=character)