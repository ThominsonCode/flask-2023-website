from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, URL, InputRequired
from flask_login import UserMixin

class RedirectionForm(FlaskForm) :
    url_to = StringField('URL', validators=[InputRequired(), URL(message='Cette URL n\'est pas valide.')])
    submit = SubmitField('Raccourcir')

class LoginForm(FlaskForm) :
    email = StringField('Email', validators=[InputRequired(), Email(message='Cet email n\'est pas valide'), Length(4, 64)])  
    password = PasswordField('Password', validators=[InputRequired(), Length(1, 64)])
    submit = SubmitField('Se connecter')
    