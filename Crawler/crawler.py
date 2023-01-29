# this is a crawler that crawls "https://www.banimode.com/new-products?sort|default=asc"

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import pymongo
# use multithreading to speed up the process
import threading
import concurrent.futures

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
            object['price'] = item.find_element(By.XPATH,"div[@class='product-card']//span[@class='price-disgit']").text
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
            object['productDiscount'] = item.find_element(By.XPATH,"div[@class='product-card']//span[@class='product-card-discount']").text
        except:
            object['productDiscount'] = ""
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

def make_driver(url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver


# mongodb database name is "ClothingSearchEngineDB" and collection name is "ClothingSearchEngineDBCollection"
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["ClothingSearchEngineDB"]
mycol = mydb["ClothingSearchEngineDBCollection"]


last_page_number = 9999


url = "https://www.banimode.com/new-products?sort|default=asc"
driver = make_driver(url)

last_page_number = find_last_page_number(driver)
urls = ["https://www.banimode.com/new-products?sort|default=asc" + str(i) for i in range(1,last_page_number+1)]

# add products to mongodb database
store_products(mycol , get_products(driver))

# print the page number
print("Page 1 is done")

# speed up the process by using multithreading

# make multi drivers for multithreading


# Run store_products five by five for urls
for i in range(0, len(urls), 5):
    # make threads
    threads = []
    for j in range(i, i+5):
        t = threading.Thread(target=store_products, args=(mycol, get_products(make_driver(urls[j]))))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    # print the page number
    print("Page " + str(i+1) + " is done")

    # for testing purposes stop after i > 20
    if i > 20:
        break




# close the driver
driver.close()


# print the number of products in the database
print("Number of products in the database: " + str(mycol.count_documents({})))



