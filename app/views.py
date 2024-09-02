from flask import render_template, url_for, flash, redirect, Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from app.models import db, User, Rental, Bicycle
from app.forms import RegistrationForm, LoginForm, RentalForm
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError
from app import bcrypt, login_manager
from datetime import datetime, date

# Create a Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users=users)

@main.route('/bikes')
def bikes():
    bicycles = Bicycle.query.filter_by(availability=True).all()
    return render_template('bikes.html', bicycles=bicycles)

@main.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data, password=hashed_password, student_id=form.student_id.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {form.name.data}!', 'success')
            return redirect(url_for('main.home'))
        except IntegrityError:
            db.session.rollback()
            flash('Student ID or email already exists. Please use different credentials.', 'danger')
    return render_template('register.html', title='Register', form=form)

@main.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('main.rent'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@main.route('/rent', methods=['GET', 'POST'])
@login_required
def rent():
    form = RentalForm()
    if form.validate_on_submit():
        bicycle = Bicycle.query.get(form.bicycle_id.data)
        if not bicycle.availability:
            flash('This bicycle is no longer available. Please select another bicycle.', 'danger')
            return redirect(url_for('main.rent'))
        
        # Proceed with rental if the bicycle is available
        rental_datetime = datetime.combine(date.today(), form.rental_time.data)
        rental = Rental(
            rental_time=rental_datetime,
            bicycle_id=form.bicycle_id.data,
            user_id=current_user.id,
            status='Rented'
        )
        
        # Update bicycle availability
        bicycle.availability = False
        
        # Save to the database
        db.session.add(rental)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash('An error occurred while processing your rental. Please try again.', 'danger')
            return redirect(url_for('main.rent'))
        
        flash('You have successfully rented the bicycle!', 'success')
        return redirect(url_for('main.home'))
    
    return render_template('rent.html', title='Rent a Bicycle', form=form)

@main.route('/return/<int:rental_id>', methods=['POST'])
@login_required
def return_bicycle(rental_id):
    rental = Rental.query.get_or_404(rental_id)

    # Check if the rental is already returned
    if rental.return_time:
        flash('This bicycle has already been returned.', 'info')
        return redirect(url_for('main.rental_history'))

    # Update the rental record with the return time
    rental.return_time = datetime.utcnow()
    rental.status = 'Returned'

    # Update bicycle availability
    rental.bicycle.availability = True

    # Save changes to the database
    db.session.commit()

    flash('You have successfully returned the bicycle!', 'success')
    return redirect(url_for('main.rental_history'))


@main.route("/rental_history")
@login_required
def rental_history():
    rentals = Rental.query.filter_by(user_id=current_user.id).all()
    return render_template('rental_history.html', rentals=rentals)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
