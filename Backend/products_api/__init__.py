from flask import Flask
from flask_restful import Api
from flask_cors import CORS
#  implement Redis cache for flask Api
from flask_redis import FlaskRedis



app = Flask(__name__)
api = Api(app)
# Resolve CORS problem
CORS(app, support_credentials=True)

# Redis configuration
app.config['REDIS_URL'] = "redis://localhost:6379/0"
# Initialize Redis
redis_store = FlaskRedis(app)




from .products import Products

api.add_resource(Products, '/products') 