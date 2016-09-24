#!/usr/bin/env python
#-*-coding: utf-8-*-
# Collect data from JingDong websites
# Python version: 2.7

"""
This program is to collect data from dynamic websites.
The dynamic websites usually use javascript to load interactive content,
such as reviews and prices which are loaded by Ajax, instead in the html source codes.
It will use MetaStudio to generate xslt script and then insert into GsExtractor.
"""

from lxml import etree
from selenium import webdriver
from GsExtractor import GsExtractor
import time

# product webpage on JingDong
url = "http://item.jd.com/1312640.html"

# use webdriver and phantomjs to load website
browser = webdriver.PhantomJS(executable_path="./phantomjs-2.1.1-macosx/bin/phantomjs")
browser.get(url)
time.sleep(5)
html = browser.execute_script("return document.documentElement.outerHTML")

# extract data from html page using xslt
doc = etree.HTML(html)

# load xslt script
jdExtra = GsExtractor()
jdExtra.setXsltFromFile("jingdong_list.xml")
result_tree = jdExtra.extract(doc)

print(str(result_tree))
