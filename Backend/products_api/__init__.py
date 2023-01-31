from flask import Flask
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app, support_credentials=True)


from .products import Products

api.add_resource(Products, '/products') 