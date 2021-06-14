import pytest
from app.app import app
from app.repository.product import Product
from app.repository.database import db

@pytest.fixture
def client():
    app.config['TESTING'] = True

    db.create_all()

    product = Product(id=1, name='TestProduct', price=5)
    db.session.add(product)
    db.session.commit()

    with app.app_context():
        with app.test_client() as client:
            yield client
    
    db.session.remove()
    db.drop_all()
    
def test_get_products(client):
    result = client.get('/product')
    print("%"*100, result)
    assert result.json == [{'id': 1, 'name': 'TestProduct', 'price': 5}]