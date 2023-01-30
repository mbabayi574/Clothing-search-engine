# a restful flask api for the project that use mongodb as database
# use swagger to test the api

from flask import Flask, jsonify, request
import pymongo


# connect to the database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ClothingSearchEngineDB"]
mycol = mydb["ClothingSearchEngineDBCollection"]

# create a flask app
app = Flask(__name__)

"""
objects in the database are like this:
{
  "_id": {
    "$oid": "63d6562c117741373a4bd260"
  },
  "productName": "شلوار جین مردانه هوگرو Hugero کد 980",
  "productBrand": "Hugero",
  "price": "893,000",
  "imageHide": "https://www.banimode.com/726812-large_default/67778.jpg",
  "imageShow": "https://www.banimode.com/726810-large_default/67778.jpg",
  "productUrl": "https://www.banimode.com/BM-67778/%D8%B4%D9%84%D9%88%D8%A7%D8%B1-%D8%AC%DB%8C%D9%86-%D9%85%D8%B1%D8%AF%D8%A7%D9%86%D9%87-%D9%87%D9%88%DA%AF%D8%B1%D9%88-hugero-%DA%A9%D8%AF-980.html#/%D8%B1%D9%86%DA%AF-%D8%B7%D9%88%D8%B3%DB%8C",
  "productDiscount": "٪10",
  "productOldPrice": "992,000 تومان"
  "isDiscount": true
}
"""

# Get products that match with one or more of the filters min_price , max_price , brand_name , have_discount , product_name
# api example: http://localhost:5000/products?min_price=100000&max_price=200000&brand_name=Hugero&have_discount=true&product_name=شلوار
# or http://localhost:5000/products?brand_name=Hugero&have_discount=true
# or http://localhost:5000/products (to get all products)
# can sort the products by price (asc or desc)
@app.route('/products', methods=['GET'])
def get_products_filter():
    # get the query parameters
    # if the parameter is not in the query then it will be None
    # if the parameter is in the query but it is empty then it will be ""
    # if the parameter is in the query and it is not empty then it will be the value of the parameter
    
    min_price = request.args.get('min_price' , default = 0 , type = int)
    max_price = request.args.get('max_price' , default = 1000000000 , type = int)
    brand_name = request.args.get('brand_name' , default = ".*" , type = str)
    have_discount = request.args.get('have_discount' , default = 0 , type = int)
    product_name = request.args.get('product_name' , default = ".*" , type = str)
    sort_flag = request.args.get('sort' , default = 0 , type = int)

    # get the products that match with the filters
    # make search_query json object
    search_query = {
        'price': {'$gte': min_price, '$lte': max_price},
    }
    if have_discount:
        search_query['isDiscount'] = True
    elif have_discount == 0:
        search_query['isDiscount'] = False

    # search in names that match with the product_name
    search_query['productName'] = {'$regex': product_name}
    # search in brands that match with the brand_name
    search_query['productBrand'] = {'$regex': brand_name}

    if ( sort_flag == 0 ):
        products = mycol.find(search_query)
    # if sort_flag == 1 then sort by price in ascending order
    elif ( sort_flag == 1 ):
        products = mycol.sort('price' , 1).find(search_query)
    # if sort_flag == 2 then sort by price in descending order
    elif ( sort_flag == 2 ):
        products = mycol.sort('price' , -1).find(search_query)
    
    # make the output json object
    output = []
    for product in products:
        output.append({
            'productName': product['productName'],
            'productBrand': product['productBrand'],
            'price': product['price'],
            'imageHide': product['imageHide'],
            'imageShow': product['imageShow'],
            'productUrl': product['productUrl'],
            'productDiscount': product['productDiscount'],
            'isDiscount': product['isDiscount'],
            'productOldPrice': product['productOldPrice']
        })
    return jsonify({'result': output})


# start the app
if __name__ == '__main__':
    app.run(debug=True)
