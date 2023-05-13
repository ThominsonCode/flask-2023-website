from myapp import app, db
from myapp.models import User, Redirection
from pathlib import Path

p = Path(__file__).resolve().parent / "instance" / "database.db"
p.unlink()

with app.app_context():
    db.create_all()
    redirection = Redirection(
        url_from = "aaaa",
        url_to = "https://www.google.fr"
    )
    user = User(
        email = "toto@toto.fr",
        password = "totototo"
    )
    db.session.add(redirection)
    db.session.add(user)
    db.session.commit()
