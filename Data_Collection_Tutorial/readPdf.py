#!/usr/bin/env python
#-*-coding: utf-8-*-
# parse pdf file using pdfminer package
# python 2.0

from urllib2 import urlopen
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, HTMLConverter
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.layout import LAParams
from cStringIO import StringIO
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfdevice import PDFDevice

def readPDF2Text(pdfFile):
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

def readPDF2HTML(pdfFile, opts={}):
    # open a PDF file
    fp = StringIO(pdfFile.read())
    retstr = StringIO()
    # create a PDF parser object associated with the file object
    parser = PDFParser(fp)
    # create a PDF document allows text extraction
    document = PDFDocument(parser) # password if needed
    # check if document allows text extraction without password
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    # create a PDF resource manager object that sotres shared resources
    rsrcmgr = PDFResourceManager()
    # create a PDF device object
    laparams = LAParams()
    for (k, v) in opts:
        if k == '-d':
            debug += 1
        elif k == '-p':
            pagenos.update(int(x) - 1 for x in v.split(','))
        elif k == '-m':
            maxpages = int(v)
        elif k == '-P':
            password = v
        elif k == '-o':
            outfile = v
        elif k == '-n':
            laparams = None
        elif k == '-A':
            laparams.all_texts = True
        elif k == '-V':
            laparams.detect_vertical = True
        elif k == '-M':
            laparams.char_margin = float(v)
        elif k == '-L':
            laparams.line_margin = float(v)
        elif k == '-W':
            laparams.word_margin = float(v)
        elif k == '-F':
            laparams.boxes_flow = float(v)
        elif k == '-Y':
            layoutmode = v
        elif k == '-O':
            outdir = v
        elif k == '-t':
            outtype = v
        elif k == '-c':
            codec = v
        elif k == '-s':
            scale = float(v)
    codec = 'utf-8'
    device = HTMLConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # create a PDF interpreter object
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pagenos = set()
    # process each page contained in the document
    for page in PDFPage.get_pages(fp, pagenos):
        interpreter.process_page(page)
    # close streams and return text content
    fp.close()
    content = retstr.getvalue()
    device.close()
    retstr.close()
    return content


url = "http://pythonscraping.com/pages/warandpeace/chapter1.pdf"
pdfFile = urlopen(url)
outputString = readPDF2Text(pdfFile)
pdfFile.close()
pdfFile = urlopen(url)
opts = map(None,['-W','-L','-t'],[0.5,0.4,'html']) # make a dictionary
outputHTML = readPDF2HTML(pdfFile, opts)
pdfFile.close()
with open("pdf_text.txt", 'w') as fout1:
    fout1.write(outputString)
    fout1.close()
with open("pdf_text.html", 'w') as fout2:
    fout2.write(outputHTML)
    fout2.close()
print("pdf to text convertion is done!")