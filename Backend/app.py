from products_api import app
#  run api in multi-threaded mode
if __name__ == '__main__':
    app.run(threaded=True, port=5000)

    
