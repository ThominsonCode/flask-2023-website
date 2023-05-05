from datetime import datetime
from myapp import db


class Redirection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_from = db.Column(db.String(20), unique=True, nullable=False)
    url_to = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"Redirection('{self.url_from}' => '{self.url_to}')"

