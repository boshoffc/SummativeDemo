from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, Length, NumberRange

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=80)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    bio = StringField('Bio', validators=[Length(max=200)])
    age = IntegerField('Age', validators=[NumberRange(min=1, max=120)])
    location = StringField('Location', validators=[Length(max=100)])
    submit = SubmitField('Register')

class UpdateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=80)])
    bio = StringField('Bio', validators=[Length(max=200)])
    age = IntegerField('Age', validators=[NumberRange(min=1, max=120)])
    location = StringField('Location', validators=[Length(max=100)])
    submit = SubmitField('Update')
