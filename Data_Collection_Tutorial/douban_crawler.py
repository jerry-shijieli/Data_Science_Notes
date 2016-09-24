#!/usr/bin/env python
#-*-coding: utf-8-*-
# Collect data from Douban websites
# Python version: 2.7

from lxml import etree
from GsExtractor import GsExtractor
from selenium import webdriver
import time

class PhantomSpider:
    def getContent(self, url):
        browser = webdriver.PhantomJS(executable_path="/Users/Jerry/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs")
        browser.get(url)
        time.sleep(3)
        html = browser.execute_script("return document.documentElement.outerHTML")
        output = etree.HTML(html)
        return output

    def saveContent(self, filepath, content):
        file_obj = open(filepath, 'w')
        file_obj.write(content)
        file_obj.close()

doubanExtra = GsExtractor()
# The following statement is ued to set up xslt formating
# first parameter is app key, second is the name of rule
doubanExtra.setXsltFromAPI("ffd5273e213036d812ea298922e2627b", "豆瓣小组讨论话题")

url = "https://www.douban.com/group/haixiuzu/discussion?start="
totalpages = 5
doubanSpider = PhantomSpider()
print("Crawling begin")

for pagenumber in range(1, totalpages):
    currenturl = url + str((pagenumber-1)*25)
    print("Crawling ", currenturl)
    content = doubanSpider.getContent(currenturl)
    outputxml = doubanExtra.extract(content)
    outputfile = "result" + str(pagenumber) + ".xml"
    doubanSpider.saveContent(outputfile, str(outputxml))

print("Data collection done!")