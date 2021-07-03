import pytest
from app.app import app
from app.repository.product import Product
from app.repository.order import BuyOrder
from app.repository.order_product import OrderProduct
from app.repository.database import db
from datetime import datetime
from test.tokens import agent_token

import logging

logger = logging.Logger(__name__)


@pytest.fixture()
def timestamp():
    return datetime(2000, 5, 5, 5, 5, 5, 5)


@pytest.fixture()
def product1(timestamp):
    return Product(
        name="TestProduct1",
        price=100,
        timestamp=timestamp,
        availability=100,
        agent_id=2,
    )


@pytest.fixture()
def product2(timestamp):
    return Product(
        name="TestProduct2",
        price=175,
        timestamp=timestamp,
        availability=100,
        agent_id=2,
    )


@pytest.fixture()
def order1(timestamp, product1):
    order = BuyOrder(
        user_name="TestName1",
        user_surname="TestSurname1",
        user_email="TestEmail1",
        user_address="TestAddress1",
        user_phone_number="TestPhoneNumber1",
        timestamp=timestamp,
    )
    order_product = OrderProduct(order=order, product=product1, quantity=2)
    order.products.append(order_product)
    return order


@pytest.fixture()
def order2(timestamp, product1, product2):
    order = BuyOrder(
        user_name="TestName2",
        user_surname="TestSurname2",
        user_email="TestEmail2",
        user_address="TestAddress2",
        user_phone_number="TestPhoneNumber2",
        timestamp=timestamp,
    )
    order_product1 = OrderProduct(
        order=order,
        product=product1,
        quantity=1,
        timestamp=timestamp,
    )
    order_product2 = OrderProduct(
        order=order,
        product=product2,
        quantity=2,
        timestamp=timestamp,
    )
    order.products.append(order_product1)
    order.products.append(order_product2)
    return order


def populate_db(product1, product2, order1, order2):
    db.session.add(product1)
    db.session.add(product2)
    db.session.add(order1)
    db.session.add(order2)
    db.session.commit()


@pytest.fixture
def client(product1, product2, order1, order2):
    app.config["TESTING"] = True

    db.create_all()

    populate_db(product1, product2, order1, order2)

    with app.app_context():
        with app.test_client() as client:
            yield client

    db.session.remove()
    db.drop_all()


def test_report_sold_units_happy(client, product2):
    # first check whether the report is correct with the initial state
    result = client.get(
        "/report/sold/2", headers={"Authorization": "Bearer " + agent_token}
    )
    assert isinstance(result.json, list)
    assert len(result.json) == 2
    assert result.json[0]["product_name"] == "TestProduct1"
    assert result.json[0]["units_sold"] == 3
    assert result.json[1]["product_name"] == "TestProduct2"
    assert result.json[1]["units_sold"] == 2

    # after that, add another order and check again
    order = BuyOrder(
        user_name="TestName3",
        user_surname="TestSurname3",
        user_email="TestEmail3",
        user_address="TestAddress3",
        user_phone_number="TestPhoneNumber3",
        timestamp=datetime(2021, 5, 5),
    )
    order_product = OrderProduct(order=order, product=product2, quantity=2)
    order.products.append(order_product)
    db.session.add(order)
    db.session.commit()

    result = client.get(
        "/report/sold/2", headers={"Authorization": "Bearer " + agent_token}
    )
    assert isinstance(result.json, list)
    assert len(result.json) == 2
    assert result.json[0]["product_name"] == "TestProduct2"
    assert result.json[0]["units_sold"] == 4
    assert result.json[1]["product_name"] == "TestProduct1"
    assert result.json[1]["units_sold"] == 3


def test_report_profit_happy(client, product1):
    # first check whether the report is correct with the initial state
    result = client.get(
        "/report/profit/2", headers={"Authorization": "Bearer " + agent_token}
    )
    assert isinstance(result.json, list)
    assert len(result.json) == 2
    assert result.json[0]["product_name"] == "TestProduct2"
    assert result.json[0]["total_profit"] == pytest.approx(350.0)
    assert result.json[1]["product_name"] == "TestProduct1"
    assert result.json[1]["total_profit"] == pytest.approx(300.0)

    # after that, add another order and check again
    order = BuyOrder(
        user_name="TestName3",
        user_surname="TestSurname3",
        user_email="TestEmail3",
        user_address="TestAddress3",
        user_phone_number="TestPhoneNumber3",
        timestamp=datetime(2021, 5, 5),
    )
    order_product = OrderProduct(order=order, product=product1, quantity=2)
    order.products.append(order_product)
    db.session.add(order)
    db.session.commit()

    result = client.get(
        "/report/profit/2", headers={"Authorization": "Bearer " + agent_token}
    )
    assert isinstance(result.json, list)
    assert len(result.json) == 2
    assert result.json[0]["product_name"] == "TestProduct1"
    assert result.json[0]["total_profit"] == pytest.approx(500.0)
    assert result.json[1]["product_name"] == "TestProduct2"
    assert result.json[1]["total_profit"] == pytest.approx(350.0)
