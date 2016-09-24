#!/usr/bin/env python
#-*-coding: utf-8-*-
# data collection from drupal gooseeker bbs

"""
This program can collect data from the static webpage of gooseeker bbs.
It works smiply by insert xslt formater obtained through the API.
The data is obtained by just converting html page into xml.
"""

from lxml import etree
from GsExtractor import GsExtractor
from six.moves import urllib

# target website
url = "http://www.gooseeker.com/cn/forum/7"
conn = urllib.request.urlopen(url)
doc = etree.HTML(conn.read())

# insert xslt formater from gooseeker API
bbsExtra = GsExtractor()
bbsExtra.setXsltFromAPI("31d24931e043e2d5364d03b8ff9cc77e", "gooseeker_bbs_xslt")
result = bbsExtra.extract(doc)

print(str(result))

