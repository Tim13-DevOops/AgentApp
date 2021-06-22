from datetime import datetime

from .database import db
from dataclasses import dataclass
from app.repository.product import Product


@dataclass
class OrderProduct(db.Model):

    product: Product
    quantity: int
    timestamp: datetime

    product_id = db.Column(
        db.Integer, db.ForeignKey("product.id"), primary_key=True
    )
    order_id = db.Column(
        db.Integer, db.ForeignKey("buy_order.id"), primary_key=True
    )
    timestamp = db.Column(db.DateTime)
    quantity = db.Column(db.Integer, default=1)
    deleted = db.Column(db.Boolean, default=False)
    product = db.relationship("Product", backref="orders")
    order = db.relationship("BuyOrder", backref="products")

    def __repr__(self):
        return f"Product {self.product.name}, Quantity: {self.quantity}"
