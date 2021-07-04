from flask_restful import Resource
from flask import jsonify
from app.services import report_service
from app.rbac import rbac


class ReportSoldAPI(Resource):
    method_decorators = {
        "get": [rbac.Allow(["agent"])],
    }

    def get(self, n_results):
        return jsonify(report_service.get_most_sold_products(n_results))


class ReportProfitAPI(Resource):
    method_decorators = {
        "get": [rbac.Allow(["agent"])],
    }

    def get(self, n_results):
        return jsonify(report_service.get_most_profitable_products(n_results))
