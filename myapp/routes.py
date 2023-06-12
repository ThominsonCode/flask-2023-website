from flask import render_template, url_for, flash, redirect
from myapp import app, db
from myapp.forms import RedirectionForm, LoginForm, SurveyForm
from myapp.models import Redirection, User, Survey, Choice, Question
from flask_login import login_user, login_required, logout_user

import random
import string

from flask import request
import requests

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
    return render_template('index.html', page_title='Accueil',redirections=redirections, form=form)


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
            flash('Connexion refusée : email ou mot de passe incorrect.', 'danger')
        else:
            flash('Connexion réussie !', 'success')
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html', page_title='Login', form=form)

@app.route("/logout/")
@login_required
def logout():
    logout_user()
    flash('Vous avez été déconnecté.', 'warning')
    return redirect(url_for('index'))

@app.route("/create_survey/", methods=['GET', 'POST'])
def create_survey():
    form = SurveyForm()
    if form.validate_on_submit():
        survey = Survey(title=form.title.data)
        for question_form in form.questions:
            question = Question(text=question_form.text.data, question_type=question_form.question_type.data)
            for choice_form in question_form.choices:
                choice = Choice(text=choice_form.text.data)
                question.choices.append(choice)
            survey.questions.append(question)
        db.session.add(survey)
        db.session.commit()
        # return redirect(url_for('index'))
    else:
        print('ne valide pas')
    return render_template('create_survey.html', page_title='Nouveau sondage', form = form)


@app.route('/proxy/', methods=['GET'])
def proxy():
    url = request.args.get('url')
    if url:
        try:
            response = requests.get(url)
            response_text = response.text
            response_text = response_text.replace('href="http://phoenixjp.net', 'href="http://192.168.1.59:5000/proxy/?url=http://phoenixjp.net')
            response_text = response_text.replace('href="..', 'href="http://192.168.1.59:5000/proxy/?url=http://www.phoenixjp.net/news/fr/..')
            response_text = response_text.replace('src="..', 'src="http://192.168.1.59:5000/proxy/?url=http://www.phoenixjp.net/news/fr/..')
            return response_text
        except requests.exceptions.RequestException as e:
            return str(e)
    else:
        return 'No URL provided.'
