from app import create_app, db
import os

app = create_app()

with app.app_context():
    os.makedirs(app.instance_path, exist_ok=True)
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
