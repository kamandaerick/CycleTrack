# populate_bicycles.py
from app import create_app, db
from app.models import Bicycle

app = create_app()

with app.app_context():
    # Define bicycle data
    bicycles_data = [
        {'model': 'BMX Bike', 'availability': True, 'image_file': 'bmx_bike.jpg'},
        {'model': 'Cargo Bike', 'availability': True, 'image_file': 'cargo_bike.jpg'},
        {'model': 'City Bike', 'availability': True, 'image_file': 'city_bike.jpg'},
        {'model': 'Cyclo Cross Bike', 'availability': True, 'image_file': 'cyclo_cross_bike.jpg'},
        {'model': 'Fat Bike', 'availability': True, 'image_file': 'fat_bike.jpg'},
        {'model': 'Gravel Bike', 'availability': True, 'image_file': 'gravel_bike.jpg'},
        {'model': 'Hybrid Bike', 'availability': True, 'image_file': 'hybrid_bicycle.jpg'},
        {'model': 'Mountain Bike', 'availability': True, 'image_file': 'mountain_bike.jpg'},
        {'model': 'Road Bike', 'availability': True, 'image_file': 'road_bicycle.jpg'},
        {'model': 'Touring Bike', 'availability': True, 'image_file': 'touring_bicycle.jpg'}
    ]

    # Add bicycles to the database
    for bike_data in bicycles_data:
        bicycle = Bicycle(
            model=bike_data['model'],
            availability=bike_data['availability'],
            image_file=bike_data['image_file']
        )
        db.session.add(bicycle)

    db.session.commit()
    print("Bicycles added successfully.")
