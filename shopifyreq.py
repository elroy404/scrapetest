# cd desktop/projects/shopify
# source scrapeify/bin/activate

import requests
import difflib
import json
from lxml import html
import platform
from bs4 import BeautifulSoup
from selenium import webdriver
import time

site_name = ""
homepage = "https://" + site_name + ".com"
url = homepage + "/sitemap_products_1.xml"
res = requests.get(url)

cart_list = []

tree = html.fromstring(res.content)

page = tree.xpath('//text()')
title = tree.xpath('//title/text()')
image_locs = tree.xpath('//image/loc/text()')
product_list = tree.xpath('//url/loc/text()')
file_og = site_name + "_og.txt"
file_new = site_name + "_new.txt"

# collects new product links
def collectLinks(new):
    new_file = open(file_new, "wb")
    print("Writing to file " + file_new + "...")
    for i in range(len(product_list)):
        new = product_list[i]
        new_file.write(new + "\n")
    new_file.close()
    print("Finished writing")

# compare og_list to new_list


# opens the product page json
def openLoc(compare):
    prod_count = len(compare)
    str_count = str(prod_count)
    for i in range(prod_count):
        json_link = compare[i] + ".json"
        print json_link
        url_pull = requests.get(json_link)
        parsed_json = json.loads(url_pull.text)
        product_title = parsed_json['product']['title']
        product_vars = parsed_json['product']['variants']
    # print("variant id\tproduct_title\t\tinventory")
        print product_title
        findVars(product_vars, parsed_json)
        print("-"*75 + "\n")

# finds variants
def findVars(vars, parsed_json):
    for i in range(len(vars)):
        var_id = parsed_json['product']['variants'][i]['id']
        var_title = parsed_json['product']['variants'][i]['title']
        # var_inv = parsed_json['product']['variants'][i]['inventory_quantity']
        str_var = str(var_id)
        cart_url = str(addCart(str_var))
        print cart_url + "\t" + str_var + "\t" + var_title
        cart_list.insert(0,cart_url)
        openBrowser(cart_list[i])

def addCart(variant):
    atc = homepage + "/cart/" + variant + ":1"
    return atc

def openBrowser(checkout):
    browser = webdriver.Chrome()
    browser.get(checkout)
    time.sleep(300)

collectLinks(file_new)
compare = compareList(file_og, file_new)
openLoc(compare)
