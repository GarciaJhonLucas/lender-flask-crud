from app import create_app
from app.db import db

app = create_app()

# Create a database
db.init_app(app)
with app.app_context():
    db.create_all() # Search Models on db