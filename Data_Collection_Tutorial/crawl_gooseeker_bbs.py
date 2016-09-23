#!/usr/bin/env python
#-*-coding:utf-8
# Visite Gooseeker forum and collect data

from six.moves import urllib
from lxml import etree
from GsExtractor import GsExtractor

# visit and read webpage content
url = "http://www.gooseeker.com/cn/forum/7"
conn = urllib.request.urlopen(url)
doc = etree.HTML(conn.read())

bbsExtra = GsExtractor()
bbsExtra.setXsltFromFile("xslt_bbs.xml")
result = bbsExtra.extract(doc)

print(str(result))