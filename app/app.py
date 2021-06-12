from flask import Flask
from flask_restful import Resource, Api
from flask_wtf.csrf import CSRFProtect
import app.config as config


from app.repository.database import init_database

app = Flask(__name__)
app.config['SECRET_KEY'] = config.FLASK_SECRET_KEY

csrf = CSRFProtect(app)
csrf.init_app(app)

api = Api(app)
db = init_database(app)

from app.api.product_api import ProductAPI

db.create_all()

api.add_resource(ProductAPI, '/product')

def main():
    app.run(host="0.0.0.0", debug=True)

if __name__ == '__main__':
    main()