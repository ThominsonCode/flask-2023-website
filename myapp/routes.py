from flask import render_template, url_for, flash, redirect
from myapp import app, db
from myapp.forms import RedirectionForm, LoginForm
from myapp.models import Redirection, User

import random
import string


@app.route('/', methods=['GET', 'POST'])
def index():
    form = RedirectionForm()
    if form.validate_on_submit():
        red = Redirection(
            url_from=''.join(random.choice(string.ascii_letters) for _ in range(4)),
            url_to=form.url_to.data
        )
        db.session.add(red)
        db.session.commit()
        return redirect(url_for('index'))

    redirections = db.session.execute(db.select(Redirection).order_by(Redirection.id.desc())).scalars()
    return render_template('index.html', redirections=redirections, form=form)


@app.route('/<string:url>')
def redirection(url):
    red = db.one_or_404(db.select(Redirection).where(Redirection.url_from == url))
    return redirect(red.url_to)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()
        if not user or form.password.data != user.password:
            flash('Email ou mot de passe incorrect', 'danger')
        else:
            flash('Connexion réussie', 'success')
    return render_template('login.html', form=form)

# test
# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#     return render_template('login.html', title='Login', form=form)
