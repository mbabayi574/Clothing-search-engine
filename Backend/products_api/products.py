from flask_restful import Resource, reqparse
from pymongo import MongoClient
from bson import json_util
import json
from flask_cors import  cross_origin

# connect to the database
myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["ClothingSearchEngineDB"]
mycol = mydb["ClothingSearchEngineDBCollection"]

# POST Request
products_data = reqparse.RequestParser()
products_data.add_argument('page', type=int, required=True, help='Page number is required')
products_data.add_argument('limit', type=int, required=True, help='Limit is required')
products_data.add_argument('min_price', type=int, required=False)
products_data.add_argument('max_price', type=int, required=False)
products_data.add_argument('product_name', type=str, required=False)
products_data.add_argument('brand_name', type=str, required=False)
products_data.add_argument('have_discount', type=int, required=False,)
products_data.add_argument('sort_flag', type=str, required=False)


class Products(Resource):
    '''
    Methods related to the Products endpoint are written 
    here.

    POST Method:
       Input: {'page':Int, 'limit':Int , 'min_price':Int, 'max_price':Int,
       'product_name':String, 'brand_name':String, 'have_discount':Int,
        'sort_flag':String} }
       Output: {'total_number':Int, 'page':Int, 
       'showing':Int, products:List}
    '''

    @cross_origin(supports_credentials=True)
    def post(self):
        data = products_data.parse_args()
     
        page = data['page']
        page_limit = data['limit']
        min_price = data['min_price']
        max_price = data['max_price']
        product_name = data['product_name']
        brand_name = data['brand_name']
        have_discount = data['have_discount']
        sort_flag = data['sort_flag']

        # If any of the filter is not provided then set it to default value
        if ( min_price == None ):
            min_price = 0
        if ( max_price == None ):
            max_price = 999999999
        if ( product_name == None ):
            product_name = ".*"
        if ( brand_name == None ):
            brand_name = ".*"
        if ( have_discount == None ):
            have_discount = 0
        if ( sort_flag == None ):
            sort_flag = "none"


        # get the products that match with the filters
        # make search_query json object
        search_query = {
            'price': {'$gte': min_price, '$lte': max_price},
        }
        if have_discount:
            search_query['isDiscount'] = True
        elif have_discount == 0:
            pass

        # search in names that match with the product_name
        search_query['productName'] = {'$regex': product_name}
        # search in brands that match with the brand_name
        search_query['productBrand'] = {'$regex': brand_name}

        # Total number of products that match with the filters
        total_number = mycol.count_documents(search_query)

        # Fetching products data and paginating

        if ( sort_flag == "none" ):
            fetch_products = mycol.find(search_query).skip(page_limit * (page - 1)).limit(page_limit)
        # if sort_flag == 1 then sort by price in ascending order
        elif ( sort_flag == "asc" ):
            fetch_products = mycol.find(search_query).sort([('price', 1)]).skip(page_limit * (page - 1)).limit(page_limit)
        # if sort_flag == 2 then sort by price in descending order
        elif ( sort_flag == "desc" ):
            fetch_products = mycol.find(search_query).sort([('price', -1)]).skip(page_limit * (page - 1)).limit(page_limit)

        products_fetched = list(json.loads(json_util.dumps(fetch_products)))

        response = {'total_number': total_number , 'last_page': ( total_number // page_limit ) + 1 , 'current_page': page, 'showing': page_limit, 'products': products_fetched}

        return response

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}