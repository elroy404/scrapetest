import requests
import os
from lxml import html

# get initial product links

site_name = "mondotees"
homepage = "https://" + site_name + ".com"
url = homepage + "/sitemap_products_1.xml"
file_og = site_name + "_og.txt"

scrapelist = os.open("/Users/geralleestes/Desktop/projects/shopify/scrapelist", os.O_RDONLY)
siteoutput = os.open("/Users/geralleestes/Desktop/projects/shopify/siteoutput", os.O_RDONLY)

def initialize(url, file_og):
    res = requests.get(url)
    tree = html.fromstring(res.content)

    page = tree.xpath('//text()')
    title = tree.xpath('//title/text()')
    image_locs = tree.xpath('//image/loc/text()')
    product_list = tree.xpath('//url/loc/text()')

    siteoutput_cd = os.fchdir(siteoutput)
    og_file = open(file_og, "wb")

    print("Writing to file " + file_og + "...")
    for i in range(len(product_list)):
        new = product_list[i]
        og_file.write(new + "\n")
    og_file.close()
    os.close(siteoutput)
    print("Finished writing")

def fileExists(url, file_og):
    siteoutput_cd = os.fchdir(siteoutput)
    if os.path.exists(file_og) != True:
        initialize(url, file_og)

if __name__ == '__main__':
    fileExists(url, file_og)
