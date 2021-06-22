import pytest
from app.app import app
from app.repository.product import Product
from app.repository.order import BuyOrder
from app.repository.order_product import OrderProduct
from app.repository.database import db
import json
from datetime import datetime


def populate_db():

    product1 = Product(
        name="TestProduct1",
        price=5,
        timestamp=datetime(2000, 5, 5, 5, 5, 5, 5),
        availability=5,
    )
    db.session.add(product1)

    product2 = Product(
        name="TestProduct2",
        price=6,
        timestamp=datetime(2006, 6, 6, 6, 6, 6, 6),
        availability=6,
    )
    db.session.add(product2)

    order1 = BuyOrder(
        user_name="TestName1",
        user_surname="TestSurname1",
        user_email="TestEmail1",
        user_address="TestAddress1",
        user_phone_number="TestPhoneNumber1",
        timestamp=datetime(2006, 6, 6, 6, 6, 6, 6),
    )
    order_product1 = OrderProduct(order=order1, product=product1, quantity=2)
    order1.products.append(order_product1)
    db.session.add(order1)

    order2 = BuyOrder(
        user_name="TestName2",
        user_surname="TestSurname2",
        user_email="TestEmail2",
        user_address="TestAddress2",
        user_phone_number="TestPhoneNumber2",
        timestamp=datetime(2006, 6, 6, 6, 6, 6, 6),
    )
    order_product2 = OrderProduct(
        order=order2,
        product=product1,
        quantity=1,
        timestamp=datetime(2006, 6, 6, 6, 6, 6, 6),
    )
    order_product3 = OrderProduct(
        order=order2,
        product=product2,
        quantity=2,
        timestamp=datetime(2006, 6, 6, 6, 6, 6, 6),
    )
    order2.products.append(order_product2)
    order2.products.append(order_product3)
    db.session.add(order2)

    db.session.commit()


@pytest.fixture
def client():
    app.config["TESTING"] = True

    db.create_all()

    populate_db()

    with app.app_context():
        with app.test_client() as client:
            yield client

    db.session.remove()
    db.drop_all()


def test_get_orders_happy(client):
    result = client.get("/order")
    assert len(result.json) == 2


def test_get_order_happy(client):
    result = client.get("/order/1")
    assert result.json["user_name"] == "TestName1"
    assert result.json["user_surname"] == "TestSurname1"
    assert result.json["user_email"] == "TestEmail1"
    assert result.json["user_address"] == "TestAddress1"
    assert result.json["user_phone_number"] == "TestPhoneNumber1"
    assert result.json["timestamp"] is not None
    assert not result.json["deleted"]


def test_get_order_sad(client):
    result = client.get("/order/1389")
    assert result.status_code == 404


def test_create_order_happy(client):
    order = {
        "user_name": "TestName3",
        "user_surname": "TestSurname3",
        "user_email": "TestEmail3",
        "user_address": "TestAddress3",
        "user_phone_number": "TestPhoneNumber3",
        "products": [(1, 3), (2, 2)],
    }

    result = client.post(
        "/order", data=json.dumps(order), content_type="application/json"
    )
    assert result.json["user_name"] == order["user_name"]
    assert result.json["user_surname"] == order["user_surname"]
    assert result.json["user_email"] == order["user_email"]
    assert result.json["user_address"] == order["user_address"]
    assert result.json["user_phone_number"] == order["user_phone_number"]
    assert len(result.json["products"]) == 2
    assert result.json["products"][0]["product"]["id"] == 1
    assert result.json["products"][0]["quantity"] == 3
    assert result.json["products"][1]["product"]["id"] == 2
    assert result.json["products"][1]["quantity"] == 2


def test_create_order_sad(client):
    order = {
        "user_name": "TestName3",
        "user_surname": "TestSurname3",
        "user_email": "TestEmail3",
        "user_address": "TestAddress3",
        "user_phone_number": "TestPhoneNumber3",
        "products": [(1, 1000)],
    }

    result = client.post(
        "/order", data=json.dumps(order), content_type="application/json"
    )
    assert result.status_code == 400
