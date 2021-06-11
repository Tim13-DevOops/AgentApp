from app.repository.product import Product

def get_products():
    products = Product.query.all()
    return products