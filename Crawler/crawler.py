# this is a crawler that crawls "https://www.banimode.com/new-products?sort|default=asc"
# TODO : 


import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import random
import pymongo
# use multithreading to speed up the process
import threading
# import Queue and Thread to use multithreading
from queue import Queue
from threading import Thread
# import WebDriverWait to wait for the page to load
from selenium.webdriver.support.ui import WebDriverWait


# get the products from the html
def get_products(driver):
    productsElements = driver.find_elements(By.XPATH,"//div[@id='product_list']/article")
    products = []

    # add objects to the products array
    # products are in a div with id "product_list" and article tag
    for idx , item in enumerate(productsElements):
        object = {}
        try:
            # object['productName'] is in "div[@class='product-card']//span[@class='product-card-name']").text
            object['productName'] = item.find_element(By.XPATH,"div[@class='product-card']//span[@class='product-card-name']").text
            # object['productBrand'] is in "div[@class='product-card']/p/a/span[@class='product-card-brand']").text
            object['productBrand'] = item.find_element(By.XPATH,"div[@class='product-card']/p/a/span[@class='product-card-brand']").text
            # object['price'] is in "div[@class='product-card']//span[@class='price-disgit']").text
            price = item.find_element(By.XPATH,"div[@class='product-card']//span[@class='price-disgit']").text
            # price is a string be like "893,000" so we need to remove the comma and convert it to int
            object['price'] = int(price.replace(",",""))
            # object['imageHide'] is in "div[@class='product-card']//img[@class='product-card-img hover-hide']").get_attribute("src")
            object['imageHide'] = item.find_element(By.XPATH,"div[@class='product-card']//img[@class='product-card-img hover-hide']").get_attribute("src")
            # object['imageShow'] is in "div[@class='product-card']//img[@class='product-card-img hover-show']").get_attribute("src")
            object['imageShow'] = item.find_element(By.XPATH,"div[@class='product-card']//img[@class='product-card-img hover-show']").get_attribute("src")
            # object['productUrl'] is in "div[@class='product-card']/a").get_attribute("href")
            object['productUrl'] = item.find_element(By.XPATH,"div[@class='product-card']/a").get_attribute("href")
        except:
            continue
        # object['productDiscount'] is in "div[@class='product-card']//span[@class='product-card-discount']").text if it exists
        try:
            productDiscount = item.find_element(By.XPATH,"div[@class='product-card']//span[@class='product-card-discount']").text
            # productDiscount is a string be like "20%" so we need to remove the "%" and convert it to int
            object['productDiscount'] = int(productDiscount.replace("٪",""))
            object['isDiscount'] = True
            
        except:
            object['productDiscount'] = 0
            object['isDiscount'] = False
        # object['productOldPrice'] is in "div[@class='product-card']//span[@class='product-card-lastprice']").text if it exists
        try:
            object['productOldPrice'] = item.find_element(By.XPATH,"div[@class='product-card']//span[@class='product-card-lastprice']").text
        except:
            object['productOldPrice'] = ""
        


        products.append(object)

    return products

# second page and others just add "&page=" + page number to the url
def find_last_page_number(driver):
    # ul with class "pagination" has li tags with "pagination-item" class that the last page number is the last item of it
    find_last_page_number = driver.find_elements(By.XPATH,"//ul[@class='pagination']/li[@class='pagination-item']")[-1].text
    return int(find_last_page_number)


def store_products(mycol , products):
    # store all_products in a mongodb database ( if already exists, update it )
    for item in products:
        # store the item in the database

        # if the item is already in the database, update it
        if mycol.find_one({"productUrl": item['productUrl']}):


            mycol.update_one(
                {"productUrl": item['productUrl']},
                {"$set": item}
            )
        # if the item is not in the database, insert it
        else:
            mycol.insert_one(item)

# initialize the driver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--disable-software-rasterizer')
options.add_argument('--disable-browser-side-navigation')
options.add_argument('--disable-features=VizDisplayCompositor')
options.add_argument('--disable-features=NetworkService')
options.add_argument('--disable-features=IsolateOrigins,site-per-process')
options.add_argument('--disable-features=site-per-process')
driver = webdriver.Chrome(options=options)

# driver timeout is 10 seconds
driver.set_page_load_timeout(10)

# if timed out from the website, try again

def make_driver(url):
    global driver
    # if timed out from the website, try again
    try:
        # wait until the page load completely
        driver.get(url)
        # for prevent ban from the website wait [0,2) seconds
        time.sleep(random.randint(0,2))
    except:
        print("timed out from the website, try again")
        driver = make_driver(url)
    return driver


# mongoDB database name is "ClothingSearchEngineDB" and collection name is "ClothingSearchEngineDBCollection"
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["ClothingSearchEngineDB"]
mycol = mydb["ClothingSearchEngineDBCollection"]


last_page_number = 9999


url = "https://www.banimode.com/new-products?sort|default=asc"
driver = make_driver(url)

last_page_number = find_last_page_number(driver)
urls = ["https://www.banimode.com/new-products?sort|default=asc&page=" + str(i) for i in range(2,last_page_number+1)]

# add products to mongodb database
store_products(mycol , get_products(driver))

# print the page number
print("First Page Work is done")

# speed up the process by using multithreading

# make multi drivers for multithreading


# run the process for urls[:6]
for url in urls[:20]:
    driver = make_driver(url)
    store_products(mycol , get_products(driver))
    print("Page " + str(urls.index(url) + 2) + " Work is done")


# test if all of products are stored in the database
print(mycol.count_documents({}))

print("All Pages Work is done")

# close the driver
driver.quit()
# close the mongodb client
myclient.close()


# TODO : use BeautifulSoup for scraping
# TODO : use multithreading for scraping



