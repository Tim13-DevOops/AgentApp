from app.repository.order_product import OrderProduct
from datetime import datetime
from .database import db
from dataclasses import dataclass, field
from typing import List


@dataclass
class BuyOrder(db.Model):
    id: int
    timestamp: datetime
    user_name: str
    user_surname: str
    user_email: str
    user_address: str
    user_phone_number: str
    deleted: bool
    products: List[OrderProduct] = field(default_factory=list)

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255))
    user_surname = db.Column(db.String(255))
    user_email = db.Column(db.String(255))
    user_address = db.Column(db.String(255))
    user_phone_number = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"BuyOrder {self.id}"
