#!/usr/bin/env python
#-*-coding: utf-8-*-
# python 2.0
# collection data from Anjuke website

from urllib2 import urlopen
from lxml import etree
from GsExtractor import GsExtractor

class Spider:
    def getContent(self, url):
        conn = urlopen(url)
        output = etree.HTML(conn.read())
        return output

    def saveContent(self, filepath, content):
        file_obj = open(filepath, 'w')
        file_obj.write(content)
        file_obj.close()

dataExtra = GsExtractor()
dataExtra.setXsltFromAPI("31d24931e043e2d5364d03b8ff9cc77e", "安居客房产经纪人")

url = "http://shenzhen.anjuke.com/tycoon/nanshan/p"
totalpages = 10
anjukeSpider = Spider()
print("Start crawling ... ")

for pagenumber in range(1, totalpages):
    currenturl = url + str(pagenumber)
    print("Crawling", currenturl)
    content = anjukeSpider.getContent(currenturl)
    outputxml = dataExtra.extract(content)
    outputfile = "result" + str(pagenumber) + ".xml"
    anjukeSpider.saveContent(outputfile, str(outputxml))

print("Crawling Done!")