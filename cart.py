import json
import requests
from diff import *

# homepage = "https://fuckingawesomestore.com/"
# homepage = "https://store.obeygiant.com/"

# opens the product page json and finds variants
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

def findVars(vars, parsed_json):
    for i in range(len(vars)):
        var_id = parsed_json['product']['variants'][i]['id']
        var_title = parsed_json['product']['variants'][i]['title']
        # var_inv = parsed_json['product']['variants'][i]['inventory_quantity']
        str_var = str(var_id)
        foo = str(addCart(str_var))
        print foo + "\t" + str_var + "\t" + var_title

def addCart(variant):
    atc = homepage + "cart/" + variant + ":1"
    return atc

openLoc(compare)
