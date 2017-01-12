# cd desktop/projects/shopify
# source scrapeify/bin/activate

import json
import requests
from lxml import html

url = ""
res = requests.get(url)

tree = html.fromstring(res.content)

page = tree.xpath('//text()')
title = tree.xpath('//title/text()')
image_locs = tree.xpath('//image/loc/text()')
product_list = tree.xpath('//url/loc/text()')

# compare diffs to product_list1 and product_list2

# print(title[0])
# print(product_list[0])
# print(image_locs[0])
# print('-'*100)

def scrapeLocs():
    # prints all links from sitemap_products_1
    for i in range(len(product_list)):
        count = str(i)
        print (count +" "+ product_list[i])
    # differing()

def differing():
    # diff.py
    # if change '+ ' then openLoc(product_loc)

# opens the product page json and finds variants
# !fix error on inventory_quantity
def openLoc(url_loc):
    url_pull = requests.get(url_loc)
    parsed_json = json.loads(url_pull.text)
    title = parsed_json['product']['title']
    product_vars = parsed_json['product']['variants']
    # print("variant id\ttitle\t\tinventory")
    for i in range(len(product_vars)):
        var_id = parsed_json['product']['variants'][i]['id']
        var_title = parsed_json['product']['variants'][i]['title']
        # var_inv = parsed_json['product']['variants'][i]['inventory_quantity']
        print(str(var_id) + "\t" + var_title)
        print("-"*75 + "\n")

def addCart():
    cart_url = requests.get("")
    # maybe open browser for checkouts
    # add to cart /cart/variant:1

product_loc = product_list[3660] + ".json"

# scrapeLocs()

# for i in range(len(title)):
#     count = str(i)
#     url_count = i
#     # print (count +" "+ title[i])
#     print (product_list[url_count])
#     # print (image_locs[i])
#     print('-' * 100)
