from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)



from .products import Products

api.add_resource(Products, '/products')