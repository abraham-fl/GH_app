from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from gh_companion.models import User


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=15)])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])

    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError("Username already exists!")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=15)])
    password = PasswordField("Password", validators=[DataRequired()])
    
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")