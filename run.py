from app import create_app, db
import os

app = create_app()

if __name__ == '__main__':
    # Ensure instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)
    with app.app_context():
        db.create_all()  # Create tables if not exist
    app.run(debug=True)
