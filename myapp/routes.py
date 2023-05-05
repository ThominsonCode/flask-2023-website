from flask import render_template, url_for, flash, redirect
from myapp import app, db
# from flaskblog.forms import RegistrationForm, LoginForm
from myapp.models import Redirection




@app.route("/")
def index():
    redirections = db.session.execute(db.select(Redirection)).scalars()
    return render_template('index.html', redirections=redirections)

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
