# from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
# from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), unique=True, nullable=False)
    password = db.Column(db.String(45), nullable=False)
    student_id = db.Column(db.String(15), unique=True, nullable=False)
    rentals = db.relationship('Rental', backref='user', lazy=True)

    def __repr__():
        return f"User: ('{self.username}', '{self.email}"

class Bicycle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(45), nullable=False)
    availability = db.Column(db.Boolean, default=True, nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default='default.jpg')
    rentals = db.relationship('Rental', backref='bicycle', lazy=True)

class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rental_time = db.Column(db.DateTime, nullable=False)
    return_time = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(45), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bicycle_id = db.Column(db.Integer, db.ForeignKey('bicycle.id'), nullable=False)
    amount_due = db.Column(db.Float, nullable=True)  # Add this field
