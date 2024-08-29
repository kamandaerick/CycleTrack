from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateTimeField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from models import Bicycle

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

class RentalForm(FlaskForm):
    bicycle_id = SelectField('Bicycle', coerce=int, validators=[DataRequired()])
    rental_time = DateTimeField('Rental Time', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    submit = SubmitField('Rent Bicycle')

    def __init__(self, *args, **kwargs):
        super(RentalForm, self).__init__(*args, **kwargs)
        self.bicycle_id.choices = [(b.id, b.model) for b in Bicycle.query.filter_by(availability=True).all()]