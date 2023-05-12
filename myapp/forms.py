from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, URL, InputRequired
from flask_login import UserMixin

class RedirectionForm(FlaskForm) :
    url_to = StringField('URL', validators=[InputRequired(), URL(message='Cette URL n\'est pas valide.')])
    submit = SubmitField('Raccourcir')

class LoginForm(FlaskForm) :
    email = StringField('Email', validators=[InputRequired(), Email(message='Cet email n\'est pas valide'), Length(4, 64)])  
    password = PasswordField('Password', validators=[InputRequired(), Length(8, 64)])


# class RegistrationForm(FlaskForm):
#     username = StringField('Username',
#                            validators=[DataRequired(), Length(min=2, max=20)])
#     email = StringField('Email',
#                         validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm_password = PasswordField('Confirm Password',
#                                      validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign Up')


# class LoginForm(FlaskForm):
#     email = StringField('Email',
#                         validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')
