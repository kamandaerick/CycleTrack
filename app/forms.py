from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=45)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=45)])
    student_id = StringField('Student ID', validators=[DataRequired(), Length(min=2, max=15)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=45)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=45)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=45)])
    submit = SubmitField('Sign In')