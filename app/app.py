from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS


from app.repository.database import init_database


app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True
CORS(app)

api = Api(app)
db = init_database(app)

from app.api.product_api import ProductAPI

db.create_all()

api.add_resource(ProductAPI, '/product')

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()