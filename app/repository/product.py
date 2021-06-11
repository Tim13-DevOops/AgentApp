from .database import db
from dataclasses import dataclass

@dataclass
class Product(db.Model):
    id: int
    name: str
    price: float

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)

    def __repr__(self):
        return f'Product {self.name}'