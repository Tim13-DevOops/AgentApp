from flask_restful import Resource
from flask import jsonify, request, abort
from app.services import product_service
from app.rbac import rbac


class ProductAPI(Resource):
    method_decorators = {
        "post": [rbac.Allow(["agent"])],
        "put": [rbac.Allow(["agent"])],
    }

    def get(self):
        return jsonify(product_service.get_products())

    def post(self):
        product_dict = request.get_json()
        return jsonify(product_service.create_product(product_dict))

    def put(self):
        product_dict = request.get_json()
        return jsonify(product_service.update_product(product_dict))


class SingleProductAPI(Resource):
    method_decorators = {
        "delete": [rbac.Allow(["agent"])],
    }

    def get(self, product_id):
        return jsonify(product_service.get_product(product_id))

    def delete(self, product_id):
        return jsonify(product_service.delete_product(product_id))
