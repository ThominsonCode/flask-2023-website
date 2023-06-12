from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, FieldList, FormField
from wtforms.validators import Length, Email, EqualTo, URL, InputRequired
from flask_login import UserMixin

class RedirectionForm(FlaskForm) :
    url_to = StringField('URL', validators=[InputRequired(), URL(message='Cette URL n\'est pas valide.')])
    submit = SubmitField('Raccourcir')

class LoginForm(FlaskForm) :
    email = StringField('Email', validators=[InputRequired(), Email(message='Cet email n\'est pas valide'), Length(4, 64)])  
    password = PasswordField('Password', validators=[InputRequired(), Length(1, 64)])
    submit = SubmitField('Se connecter')


class ChoiceForm(FlaskForm):
    text = StringField(label='Choix', validators=[InputRequired()])


class QuestionForm(FlaskForm):
    text = StringField('Texte de la question :', validators=[InputRequired()])
    question_type = SelectField('Type de question :', choices=[('radio', 'Radio'), ('checkbox', 'Checkbox'), ('textfield', 'Text Field'), ('textarea', 'Text Area')], validators=[InputRequired()])
    choices = FieldList(FormField(ChoiceForm), min_entries=2)

    def __init__(self, formdata=..., **kwargs):
        super().__init__(formdata, **kwargs)
        for index, choice in enumerate(self.choices):
            choice.form.text.label.text = f"Choix {index + 1}"


class SurveyForm(FlaskForm):
    title = StringField('Titre du sonsage :', validators=[InputRequired()])
    questions = FieldList(FormField(QuestionForm), min_entries=2)
    submit = SubmitField('Submit')