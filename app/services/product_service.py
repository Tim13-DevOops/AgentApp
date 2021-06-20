from datetime import datetime

from app.repository.product import Product
from app.repository.database import db

def get_products():
    products = Product.query.filter_by(deleted=False).all()
    return products

def get_product(product_id):
    products = Product.query.filter_by(id=product_id).first()
    return products

def create_product(product_dict):
    product_dict.pop('id', None)
    product = Product(**product_dict)
    product.timestamp = datetime.now()
    db.session.add(product)
    db.session.commit()
    return product

def update_product(product_dict):
    query = Product.query.filter_by(id=product_dict['id'])
    product = query.first()
    query.update(product_dict)
    db.session.commit()
    return product

def delete_product(product_id):
    query = Product.query.filter_by(id=product_id)
    product = query.first()
    query.update({'deleted': True})
    db.session.commit()
    return product