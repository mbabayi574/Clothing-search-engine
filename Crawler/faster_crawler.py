# Use Both of Selenium and BeautifulSoup to crawl the data

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time, random

# Define A Function For Making Driver
def make_driver(url):
    options = webdriver.ChromeOptions()
    # Make it headless
    options.add_argument('--headless')
    # Make it not to show the browser
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    try:
        # Wait 10 seconds for the page to load
        driver.set_page_load_timeout(10)
        # wait until the page load completely
        driver.get(url)
    # if TimeoutException occurs, try again
    except TimeoutException:
        driver.set_page_load_timeout(20)
        driver.get(url)
    # if exception occurs again, return None
    except:
        print("\nfaild to load" + url + " page\n")
        return None

    # get the html of the page
    html = driver.page_source
    # close the driver
    driver.close()

    # for prevent ban from the website wait [0,2) seconds
    time.sleep(random.randint(0,2))

    return html

# Define a functoion for parsing the html and extracting products from it

from bs4 import BeautifulSoup

def parse_html(html):
    products = []
    soup = BeautifulSoup(html, 'html.parser')
    # Find all the products in the page ( article of a div with id 'product_list' )
    products_section = soup.find('div', id='product_list').find_all('article')
    for product in products_section:
        object = {}
        product_card = product.find('div', class_='product-card')
        try:
            # object['productName'] is in product_card > span ( class = 'product-card-name' )
            object['productName'] = product_card.find('span', class_='product-card-name').text
            # object['productBrand'] is in product_card > p > a > span ( class = 'product-card-brand' )
            object['productBrand'] = product_card.find('p').find('a').find('span', class_='product-card-brand').text
            # object['price'] is in product_card > span ( class = 'price-disgit' )
            price = product_card.find('span', class_='price-disgit').text
            object['price'] = int(price.replace(",",""))
            # object['imageHide'] is in product_card > img ( class = 'product-card-img hover-hide' ) > src
            object['imageHide'] = product_card.find('img', class_='product-card-img hover-hide').get('src')
            # object['imageShow'] is in product_card > img ( class = 'product-card-img hover-show') > src
            object['imageShow'] = product_card.find('img', class_='product-card-img hover-show').get('src')
            # object['productUrl'] is in product_card > a ( class = 'product-card-img-link' ) > href
            object['productUrl'] = product_card.find('a', class_='product-card-img-link').get('href')

        except:
            continue
        
        # Find Discount
        try:
            # object['productDiscount'] is in product_card > span ( class = 'product-card-discount') if it exists
            productDiscount = product_card.find('span', class_='product-card-discount').text
            object['productDiscount'] = int(productDiscount.replace("٪",""))
            object['isDiscount'] = True
        except:
            object['productDiscount'] = 0
            object['isDiscount'] = False
        # Find Old Price
        try:
            # object['productOldPrice'] is in product_card > span ( class = 'product-card-lastprice' ) if it exists
            object['productOldPrice'] = product_card.find('span', class_='product-card-lastprice').text
        except:
            object['productOldPrice'] = ""

        products.append(object)

    return products

import pymongo

# mongoDB database name is "ClothingSearchEngineDB" and collection name is "ClothingSearchEngineDBCollection"
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["ClothingSearchEngineDB"]
mycol = mydb["ClothingSearchEngineDBCollection"]

# Define a function for saving the products in a mongoDB database
def save_products(mycol , products):
    # store all_products in a mongodb database ( if already exists, update it )
    for item in products:
        if mycol.find_one({"productUrl": item['productUrl']}):
            mycol.update_one(
                {"productUrl": item['productUrl']},
                {"$set": item}
            )
        else:
            mycol.insert_one(item)


"""
We Must Define A Function For Getting The Last Page Number
This is in the pagination section of the page
ul ( class = "pagination" ) > li ( class = "pagination-item" )[-1].text
"""

def find_last_page_number(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Find the last page number in the pagination section
    last_page_number = soup.find('ul', class_='pagination').find_all('li', class_='pagination-item')[-1].text
    return int(last_page_number)



# find the last page number and save it in last_page_number and extract the products from the first page
html = make_driver('https://www.banimode.com/new-products?sort|default=asc&page=1')
last_page_number = find_last_page_number(html)
products = parse_html(html)
save_products(mycol, products)
print("Page 1 Done And Products Saved")

""" Import Parallel Python Library for run make_driver and parse_html and save_products in three different threads

    first thread: make_driver
    second thread: parse_html
    third thread: save_products

    if a function operation is done, then pass the result to the next function and start for the next page
    wait until the last page is reached

"""

# Start The Crawler ( It will run until the last page is reached )

def page_operation(page_number):
    # Make Driver
    html = make_driver('https://www.banimode.com/new-products?sort|default=asc&page=' + str(page_number))
    # Parse Html
    products = parse_html(html)
    # Save Products
    save_products(mycol, products)
    print(f"Page {page_number} Done And Products Saved")

"""
make six threads for run page_operation function

in each thread, we pass a page number to the page_operation function
"""
from multiprocessing import Pool

with Pool(6) as p:
    p.map(page_operation, range(2, last_page_number + 1))

# Close The Connection
myclient.close()




