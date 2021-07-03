import pytest
import json
from app.app import app
from app.repository.product import Product
from app.repository.database import db
from datetime import datetime
from flask import jsonify
from test.tokens import agent_token


def populate_db():

    product = Product(
        name="TestProduct1",
        price=5,
        timestamp=datetime(2000, 5, 5, 5, 5, 5, 5),
        availability=5,
        image="image1.jpg",
        agent_id=2,
    )
    db.session.add(product)
    db.session.commit()

    product = Product(
        name="TestProduct2",
        price=6,
        timestamp=datetime(2006, 6, 6, 6, 6, 6, 6),
        availability=6,
        image="image1.jpg",
        agent_id=2,
    )
    db.session.add(product)
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


def test_get_products_happy(client):
    result = client.get("/product")
    assert len(result.json) == 2


def test_get_product_happy(client):
    result = client.get("/product/1")
    assert result.json["name"] == "TestProduct1"
    assert result.json["price"] == 5
    assert result.json["timestamp"] != None
    assert result.json["availability"] == 5
    assert result.json["deleted"] == False
    assert result.json["image"] == "image1.jpg"


def test_get_product_sad(client):
    result = client.get("/product/1389")
    assert result.status_code == 404


def test_create_product_happy(client):
    product = {
        "name": "TestProduct3",
        "price": 7,
        "availability": 7,
        "image": "image1.jpg",
    }

    result = client.post(
        "/product",
        data=json.dumps(product),
        content_type="application/json",
        headers={"Authorization": "Bearer " + agent_token},
    )
    print(result.json)
    assert result.json["name"] == product["name"]
    assert result.json["price"] == product["price"]
    assert result.json["availability"] == product["availability"]
    assert result.json["timestamp"] != None
    assert result.json["deleted"] == False
    assert result.json["id"] != None
    assert result.json["image"] == product["image"]


def test_create_product_sad(client):
    product = {"name": "TestProduct3", "price": "cheap", "availability": 7}

    result = client.post(
        "/product",
        data=json.dumps(product),
        content_type="application/json",
        headers={"Authorization": "Bearer " + agent_token},
    )
    assert result.status_code == 500


def test_update_product_happy(client):
    product = {
        "id": 2,
        "name": "TestProduct2Updated",
        "price": 12,
        "availability": 12,
        "image": "image1.jpg",
    }

    result = client.put(
        "/product",
        data=json.dumps(product),
        content_type="application/json",
        headers={"Authorization": "Bearer " + agent_token},
    )
    assert result.json["name"] == product["name"]
    assert result.json["price"] == product["price"]
    assert result.json["availability"] == product["availability"]
    assert result.json["timestamp"] != None
    assert result.json["deleted"] == False
    assert result.json["id"] == product["id"]
    assert result.json["image"] == product["image"]


def test_update_product_sad(client):
    product = {
        "id": 1389,
        "name": "TestProduct2Updated",
        "price": 12,
        "availability": 12,
    }
    result = client.put(
        "/product",
        data=json.dumps(product),
        content_type="application/json",
        headers={"Authorization": "Bearer " + agent_token},
    )
    assert result.status_code == 404


def test_delete_product_happy(client):
    product_id = 1
    result = client.delete(
        f"/product/{product_id}", headers={"Authorization": "Bearer " + agent_token}
    )
    assert result.json["id"] == product_id
    assert result.json["deleted"] == True


def test_delete_product_sad(client):
    product_id = 1389
    result = client.delete(
        f"/product/{product_id}", headers={"Authorization": "Bearer " + agent_token}
    )
    assert result.status_code == 404
