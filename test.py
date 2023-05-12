from myapp import app, db
from myapp.models import User

with app.app_context():
    # db.create_all()