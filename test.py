import requests
import urllib2
from lxml import html

from multiprocessing import Pool

site_name = "cyclopsprintworks"
homepage = "https://" + site_name + ".com"
url = homepage + "/sitemap_products_1.xml"

urls = [
  'https://mondotees.com/sitemap_products_1.xml',
  'https://cyclopsprintworks.com/sitemap_products_1.xml',
  'https://bottleneckgallery.com/sitemap_products_1.xml',
  'https://greymatterart.com/sitemap_products_1.xml',
  'https://obeygiant.com/sitemap_products_1.xml'
  ]

# tree = html.fromstring(res.content)
# product_list = tree.xpath('//url/loc/text()')

def collectLinks(url):
    session = requests.Session()
    stuff_got = []
    
    res = session.get(urls)
    return res

pool = Pool()

results = pool.map(collectLinks, urls)
print results
pool.close()
pool.join()
