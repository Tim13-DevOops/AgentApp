from flask_restful import Resource
from flask import jsonify
from app.services import product_service


class ProductAPI(Resource):
    def get(self):
        return jsonify(product_service.get_products())

    