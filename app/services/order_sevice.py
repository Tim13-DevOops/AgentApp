from app.repository.order_product import OrderProduct
from app.repository.order import BuyOrder
from app.repository.product import Product
from app.repository.database import db
from datetime import datetime
from logging import Logger
from flask import abort

logger = Logger(__name__)


def get_orders():
    orders = BuyOrder.query.filter_by(deleted=False).all()
    return orders


def get_order(order_id):
    order = BuyOrder.query.filter_by(id=order_id).first()
    if order is None:
        abort(404)
    return order


def create_order(order_dict):
    """Creates an order and order product relationship for each product.

    Args:
            order_dict: dict with keys:
                'user_name', 'user_surname', 'user_email', 'user_address',
                'user_phone_number' 'products': which is a list of tuples with
                product and quantity.
    """
    order = BuyOrder(
        user_name=order_dict["user_name"],
        user_surname=order_dict["user_surname"],
        user_email=order_dict["user_email"],
        user_address=order_dict["user_address"],
        user_phone_number=order_dict["user_phone_number"],
    )
    order.timestamp = datetime.now()
    for product_id, quantity in order_dict.get("products", []):
        product_query = Product.query.filter_by(id=product_id)
        product = product_query.first()
        if product.availability < quantity:
            db.session.rollback()
            abort(400, f"not enough {product.name} in stock")
        product_query.update(
            {"availability": (Product.availability - quantity)}
        )
        order_product = OrderProduct(
            order=order, product=product, quantity=quantity
        )
        order_product.timestamp = datetime.now()
        order.products.append(order_product)
    db.session.add(order)
    db.session.commit()
    return order
