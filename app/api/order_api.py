from flask_restful import Resource
from flask import jsonify, request
from app.services import order_sevice


class OrderAPI(Resource):
    def get(self):
        return jsonify(order_sevice.get_orders())

    def post(self):
        order_dict = request.get_json()
        return jsonify(order_sevice.create_order(order_dict))


class SingleOrderAPI(Resource):
    def get(self, order_id):
        return jsonify(order_sevice.get_order(order_id))
