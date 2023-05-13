from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = "Vous devez être connecté pour accéder à cette ressource."
login_manager.login_message_category = "danger"

from myapp import routes
from myapp.models import User


@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(User).where(User.id == str(user_id))).scalar()