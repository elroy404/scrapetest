import requests
from lxml import html

# get initial product links

site_name = "store.obeygiant"
homepage = "https://" + site_name + ".com"
url = homepage + "/sitemap_products_1.xml"
res = requests.get(url)

tree = html.fromstring(res.content)

page = tree.xpath('//text()')
title = tree.xpath('//title/text()')
image_locs = tree.xpath('//image/loc/text()')
product_list = tree.xpath('//url/loc/text()')
file_og = site_name + "_og.txt"

og_file = open(file_og, "wb")

print("Writing to file " + file_og + "...")
for i in range(len(product_list)):
    new = product_list[i]
    og_file.write(new + "\n")
og_file.close()
print("Finished writing")
