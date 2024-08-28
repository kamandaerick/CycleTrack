from flask import Flask
from models import db, User
from flask import render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_bcrypt import Bcrypt



app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bicycle_rental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.secret_key = 'dev'

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users = users)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #Logic to add the user to the db
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data, password=hashed_password, student_id=form.student_id.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.name.data}!', 'success')
        #Redirect the registered user to the homepage return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

#create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)