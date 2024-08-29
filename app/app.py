from flask import Flask
from models import db, User
from flask import render_template, url_for, flash, redirect
from flask_login import LoginManager, login_user, logout_user, login_required
from forms import RegistrationForm, LoginForm
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError



app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bicycle_rental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.secret_key = 'dev'

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

@app.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users = users)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data, password=hashed_password, student_id=form.student_id.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {form.name.data}!', 'success')
            return redirect(url_for('home'))
        except IntegrityError:
            db.session.rollback()  # Roll back the session to prevent it from being in an invalid state
            flash('Student ID or email already exists. Please use different credentials.', 'danger')
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
#create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)