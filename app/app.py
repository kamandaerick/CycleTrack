from flask import Flask
from models import db

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bicycle_rental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Welcome to CycleTrack</h1> <br> <h3>Your favourite Bicycle Renting App</h3>'

#create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)