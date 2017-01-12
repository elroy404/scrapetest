# source scrapeify/bin/activate

import platform
from bs4 import BeautifulSoup
from selenium import webdriver
from lxml import etree
from lxml import url
import timeit

start = timeit.timeit()
browser = webdriver.PhantomJS()
browser.get('https://mondotees.com/sitemap_products_1.xml')

soup = BeautifulSoup(browser.page_source, "xml")
product = soup.find_all('loc')
productInvNum = len(product)


for i in range(productInvNum):
    print(product[i])

# print(products[3658])

end = timeit.timeit()
print(end - start)
browser.close()
