from flask_restful import Resource
from flask import jsonify, request
from app.services import order_sevice
from app.rbac import rbac


class OrderAPI(Resource):
    method_decorators = {
        "get": [rbac.Allow(["agent"])],
    }

    def get(self):
        return jsonify(order_sevice.get_orders())

    def post(self):
        order_dict = request.get_json()
        return jsonify(order_sevice.create_order(order_dict))


class SingleOrderAPI(Resource):
    method_decorators = {
        "get": [rbac.Allow(["agent"])],
    }

    def get(self, order_id):
        return jsonify(order_sevice.get_order(order_id))
