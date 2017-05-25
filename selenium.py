#!/usr/bin/python3
# -*- coding: utf8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.yourator.co/jobs"

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get(url)

with open('source.html','w') as f:
	f.write(driver.page_source)
print('===============')
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
with open('execute.html','w') as f:
	f.write(html)
driver.close()