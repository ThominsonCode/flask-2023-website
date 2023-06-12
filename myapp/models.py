from datetime import datetime
from myapp import db
from flask_login import UserMixin
from sqlalchemy import Enum


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    
    redirections = db.relationship('Redirection', backref='user')


class Redirection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_from = db.Column(db.String(20), unique=True, nullable=False)
    url_to = db.Column(db.String(120), unique=False, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey(User.id), unique=False, nullable=True)

    def __repr__(self):
        return f"Redirection('{self.url_from}' => '{self.url_to}')"


class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    questions = db.relationship('Question', backref='survey')


class Question(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120), nullable=False)
    question_type = db.Column(Enum('radio', 'checkbox', 'textfield', 'textarea'), nullable=False)
    choices = db.relationship('Choice', backref='question')
    survey_id = db.Column(db.Integer, db.ForeignKey(Survey.id), nullable=False)


class Choice(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey(Question.id), nullable=False)

