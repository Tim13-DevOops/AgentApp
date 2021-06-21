from flask_restful import Resource
from flask import jsonify
from app.services import report_service


class ReportSoldAPI(Resource):
    def get(self, n_results):
        return jsonify(report_service.get_most_sold_products(n_results))


class ReportProfitAPI(Resource):
    def get(self, n_results):
        return jsonify(report_service.get_most_profitable_products(n_results))
