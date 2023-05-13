from myapp import app, db
from myapp.models import User, Redirection
from pathlib import Path

p = Path(__file__).resolve().parent / "instance" / "database.db"
p.unlink()

with app.app_context():
    db.create_all()
    red1 = Redirection(
        url_from = "aaaa",
        url_to = "https://www.google.fr"
    )
    db.session.add(red1)

    user1 = User(
        email = "toto@toto.fr",
        password = "totototo"
    )
    db.session.add(user1)
    db.session.commit()

    red2 = Redirection(
        user = user1.id,
        url_from = "bbbb",
        url_to = "https://www.duckduckgo.com"
    )
    db.session.add(red2)
    red2 = Redirection(
        user = user1.id,
        url_from = "cccc",
        url_to = "https://www.ecosia.com"
    )
    db.session.add(red2)
    db.session.commit()

    red = db.session.execute(db.select(Redirection).where(Redirection.user == user1.id)).scalars()
    print([r for r in red])
