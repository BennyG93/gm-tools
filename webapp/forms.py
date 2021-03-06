from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired, NumberRange

class GMLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class QuickScoutForm(FlaskForm):
    total_turns = IntegerField('Total turns to use', validators=[DataRequired(), NumberRange(min=1, message="Invalid number of turns")])
    turns_interval = IntegerField('Amount of turns per click', validators=[DataRequired(), NumberRange(min=1, max=300, message="Invalid number of turns")])
    scout_choices = RadioField('Scout Option', choices=[('casino', 'Go to Casino'), ('coffee', 'Go to Coffee'), ('streets', 'Go to the streets'), ('training', 'Go to training rooms')], validators=[DataRequired()])
    headless = BooleanField('Run headless?')
    submit = SubmitField('Scout')
