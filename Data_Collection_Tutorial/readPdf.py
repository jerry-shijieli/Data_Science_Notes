#!/usr/bin/env python
#-*-coding: utf-8-*-
# parse pdf file using pdfminer package
# python 2.0

from urllib2 import urlopen
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
from cStringIO import StringIO

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pagenos = set()
    fp = StringIO(pdfFile.read())
    for page in PDFPage.get_pages(fp, pagenos):
        interpreter.process_page(page)
    fp.close()
    device.close()
    content = retstr.getvalue()
    retstr.close()
    return content

pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()