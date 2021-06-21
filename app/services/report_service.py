from app.repository.product import Product
from app.repository.order_product import OrderProduct
from app.repository.database import db
from sqlalchemy import func, desc

import logging

logger = logging.Logger(__name__)


def get_most_sold_products(n_results):
    result = (
        db.session.query(
            Product.id,
            Product.name,
            func.coalesce(func.sum(OrderProduct.quantity), 0).label(
                "total_sold"
            ),
        )
        .select_from(Product)
        .join(OrderProduct, Product.id == OrderProduct.product_id, isouter=True)
        .group_by(Product.id)
        .order_by(desc("total_sold"))
        .limit(n_results)
        .all()
    )
    result = [
        {"product_id": row[0], "product_name": row[1], "units_sold": row[2]}
        for row in result
    ]

    return result


def get_most_profitable_products(n_results):
    result = (
        db.session.query(
            Product.id,
            Product.name,
            (
                func.coalesce(
                    func.sum(OrderProduct.quantity) * Product.price, 0
                )
            ).label("total_profit"),
        )
        .select_from(Product)
        .join(OrderProduct, Product.id == OrderProduct.product_id, isouter=True)
        .group_by(Product.id)
        .order_by(desc("total_profit"))
        .limit(n_results)
        .all()
    )
    result = [
        {"product_id": row[0], "product_name": row[1], "total_profit": row[2]}
        for row in result
    ]

    return result
