from flask import render_template, url_for, flash, redirect
from myapp import app, db
from myapp.forms import RedirectionForm
from myapp.models import Redirection

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
