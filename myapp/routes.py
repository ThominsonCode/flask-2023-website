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
        redirection = Redirection(
            url_from = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6)),
            url_to = form.url_to.data
        )
        db.session.add(redirection)
        db.session.commit()
        return redirect(url_for('index'))

    redirections = db.session.execute(db.select(Redirection)).scalars()
    return render_template('index.html', redirections=redirections, form=form)

# c
# @app.route("/about")
# def about():
#     return render_template('about.html', title='About')


# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template('register.html', title='Register', form=form)


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
