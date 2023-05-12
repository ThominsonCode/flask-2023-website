from datetime import datetime
from myapp import db
from flask_login import UserMixin

class Redirection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_from = db.Column(db.String(20), unique=True, nullable=False)
    url_to = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"Redirection('{self.url_from}' => '{self.url_to}')"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
  