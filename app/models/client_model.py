from app.db import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    document = db.Column(db.String(11), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "document": self.document,
            "address": self.address,
            "phone": self.phone,
            "status": self.status,
        }
