import os
from flask import Flask, make_response
from flask_migrate import Migrate
from flask_migrate import init as migrate_init
from flask_migrate import migrate as migrate_migrate
from flask_migrate import upgrade as migrate_upgrade
from flask_cors import CORS
from prometheus_flask_exporter import RESTfulPrometheusMetrics
import app.config as config
from app.custom_api import CustomApi

from app.repository.database import init_database

app = Flask(__name__)
app.config["SECRET_KEY"] = config.SECRET_KEY
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


cors = CORS(app, resources={r"/*": {"origins": "localhost"}})

api = CustomApi(app)
db = init_database(app)
metrics = RESTfulPrometheusMetrics(app, api)

from app.rbac import rbac

rbac.setJWTManager(app)

from app.api.product_api import ProductAPI, SingleProductAPI
from app.api.order_api import OrderAPI, SingleOrderAPI
from app.api.report_api import ReportSoldAPI, ReportProfitAPI

migrate = Migrate(app, db)

api.add_resource(ProductAPI, "/product")
api.add_resource(SingleProductAPI, "/product/<int:product_id>")
api.add_resource(OrderAPI, "/order")
api.add_resource(SingleOrderAPI, "/order/<int:order_id>")
api.add_resource(ReportSoldAPI, "/report/sold/<int:n_results>")
api.add_resource(ReportProfitAPI, "/report/profit/<int:n_results>")

from app.prometheus_metrics.prometheus_metrics import (
    init_metrics,
)

init_metrics()


@api.representation("application/octet-stream")
def output_stream(data, code, headers=None):
    """Makes a Flask response with a bytes body"""
    resp = make_response(data, code)
    resp.headers.extend(headers or {})
    return resp


def db_migrate():
    with app.app_context():
        if not os.path.exists("./migrations"):
            migrate_init()
        migrate_migrate()
        migrate_upgrade()


def main():
    app.run(host="0.0.0.0", port=config.FLASK_PORT, debug=True)


if __name__ == "__main__":
    main()
