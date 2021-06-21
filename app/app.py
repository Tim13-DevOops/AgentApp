import os

from flask import Flask
from flask.wrappers import Response
from flask_restful import Api
from flask_migrate import Migrate
from flask_migrate import init as migrate_init
from flask_migrate import migrate as migrate_migrate
from flask_migrate import upgrade as migrate_upgrade
from flask_cors import CORS
import app.config as config
import json

from app.repository.database import init_database

app = Flask(__name__)
app.config["SECRET_KEY"] = config.FLASK_SECRET_KEY
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# csrf = CSRFProtect(app)
# csrf.init_app(app)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

api = Api(app)
db = init_database(app)

from app.api.product_api import ProductAPI, SingleProductAPI
from app.api.order_api import OrderAPI, SingleOrderAPI

migrate = Migrate(app, db)

api.add_resource(ProductAPI, "/product")
api.add_resource(SingleProductAPI, "/product/<int:product_id>")
api.add_resource(OrderAPI, "/order")
api.add_resource(SingleOrderAPI, "/order/<int:order_id>")


@app.errorhandler(Exception)
def handle_exception(error):
    response = Response()
    response.data = json.dumps(
        {
            "code": 500,
            "name": "Internal server error",
        }
    )
    response.status_code = 500
    response.content_type = "application/json"
    return response


def db_migrate():
    with app.app_context():
        if not os.path.exists("./migrations"):
            migrate_init()
            # os.remove('./migrations')
        migrate_migrate()
        migrate_upgrade()


def main():
    app.run(host="0.0.0.0", debug=True)


if __name__ == "__main__":
    main()
