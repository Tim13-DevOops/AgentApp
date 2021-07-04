from datetime import datetime
from flask import abort
from app.repository.product import Product
from app.repository.database import db
from app.rbac import rbac


def get_products():
    user = rbac.get_current_user()

    if user.user_role == "agent":
        products = Product.query.filter_by(deleted=False, agent_id=user.id).all()
        return products
    else:
        products = Product.query.filter_by(deleted=False).all()
        return products


def get_product(product_id):
    product = Product.query.filter_by(id=product_id).first()
    if product == None:
        abort(404)
    return product


def create_product(product_dict):
    user = rbac.get_current_user()
    product_dict["agent_id"] = user.id
    product_dict.pop("id", None)
    product = Product(**product_dict)
    product.timestamp = datetime.now()
    db.session.add(product)
    db.session.commit()
    return product


def update_product(product_dict):
    user = rbac.get_current_user()
    query = Product.query.filter_by(id=product_dict["id"])
    product = query.first()

    if product == None:
        abort(404, f'Invalid product id {product_dict["id"]}')
    if product.agent_id != user.id:
        abort(404, "Product does not belog to this agent")

    query.update(product_dict)
    db.session.commit()
    return product


def delete_product(product_id):
    user = rbac.get_current_user()
    query = Product.query.filter_by(id=product_id)
    product = query.first()

    if product == None:
        abort(404, f"Invalid product id {product_id}")
    if product.agent_id != user.id:
        abort(404, "Product does not belog to this agent")

    query.update({"deleted": True})
    db.session.commit()
    return product
