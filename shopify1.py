# source scrapeify/bin/activate

import platform
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://store.obeygiant.com/cart/11130640897:1"

browser = webdriver.Chrome()
browser.get(url)
