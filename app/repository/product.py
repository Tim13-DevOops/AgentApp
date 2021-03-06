from datetime import datetime
from .database import db
from dataclasses import dataclass


@dataclass
class Product(db.Model):
    id: int
    timestamp: datetime
    name: str
    price: float
    availability: int
    deleted: bool
    image: str
    agent_id: int

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)
    availability = db.Column(db.Integer)
    deleted = db.Column(db.Boolean, default=False)
    image = db.Column(db.String(255))
    agent_id = db.Column(db.Integer)

    def __repr__(self):
        return f"Product {self.name}"
