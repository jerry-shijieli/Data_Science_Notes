#!/usr/bin/env python
#-*-encoding:utf-8-*-
import urllib2
import BeautifulSoup
import re

# Search an article on topic of 'on random graph' on Google scholar
query = 'on+random+graph'
url = 'http://scholar.google.com/scholar?hl=en&q=' + query + '&btnG=&as_sdt=1%2C34&as_stdp='

# 设置头文件。抓取有些的网页不需要专门设置头文件，但是这里如果不设置的话，
# google会认为是机器人不允许访问。另外访问有些网站还有设置Cookie，这个会相对复杂一些，
# 这里暂时不提。关于怎么知道头文件该怎么写，一些插件可以看到你用的浏览器和网站交互的
# 头文件（这种工具很多浏览器是自带的），我用的是firefox的firebug插件。

header = {'Host': 'scholar.google.com',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0',
'Referer': 'https://scholar.google.com/',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':	'en-US,en;q=0.5',
'Connection': 'keep-alive'}

# set connection 
req = urllib2.Request(url, headers=header)
#req = urllib2.Request(url)
con = urllib2.urlopen(req)

# read html content
doc = con.read()

# Close connection
con.close()

# create soup
soup = BeautifulSoup.BeautifulSoup(doc)

# 抓取论文标题，作者，简短描述，引用次数，版本数，引用它的文章列表的超链接
# 这里还用了一些正则表达式，不熟悉的先无知它好了。至于'class' : 'gs_rt'中
# 'gs_rt'是怎么来的，这个是分析html文件肉眼看出来的。上面提到的firebug插件
# 让这个变的很简单，只要一点网页，就可以知道对应的html 标签的位置和属性，
# 相当好用。
paper_name = soup.html.body.find('h3', {'class': 'gs_rt'}).text
paper_name = re.sub(r'\[.*\]', '', paper_name) # eliminate '[]' tags like '[PDF]'
paper_author = soup.html.body.find('div', {'class': 'gs_a'}).text
paper_desc = soup.html.body.find('div', {'class': 'gs_rs'}).text
temp_str = soup.html.body.find('div', {'class':'gs_fl'}).text
temp_re = re.match(r'[A-Za-z\s]+(\d*)[A-Za-z\s]+(\d*)', temp_str)
citeTimes = temp_re.group(1)
versionNum = temp_re.group(2)
if citeTimes == '':
	citeTimes = '0'
if versionNum == '':
	versionNum = '0'

citedPaper_herf = soup.html.body.find('div', {'class': 'gs_fl'}).a.attrs[0][1]

# 打开文件webdata.txt，生成对象file,这个文件可以是不存在的，参数a表示往里面添加。
# 还有别的参数，比如'r'只能读但不能写入，'w'可以写入但是会删除原来的记录等等
file = open('webdata.txt','a')
line = paper_name + '#' + paper_author + '#' + paper_desc + '#' + citeTimes + '\n'
# 对象file的write方法将字符串line写入file中.鏈枃鍘熷垱鑷�1point3acres璁哄潧
file = file.write(line)
# 再一次的，做个随手关闭文件的好青年
file.close()