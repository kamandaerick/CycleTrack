from app import db, create_app
from app.models import Bicycle
app = create_app()
def delete_all_bicycles():
    # Query all bicycles and delete them
    Bicycle.query.delete()
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        delete_all_bicycles()
