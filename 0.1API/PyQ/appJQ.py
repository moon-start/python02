## 安裝 python -m pip install --upgrade pip
## 安裝 pip install pyquery

from pyquery import PyQuery as pq

# ## （1）直接字符串
# ## doc現在就相當於jQuery裡面的$符號了
# doc = pq("<html></html>")
# ## （2）lxml.etree
# from lxml import etree
# doc = pq(etree.fromstring("<html></html>"))
# ## （3）直接傳URL
# doc = pq('http://www.baidu.com')
# ## （4）傳文件
# doc = pq(filename='hello.html')



## 使用
doc = pq(filename='./0.1API/hello.html')
print( doc.html()  )
print( type(doc) )
li = doc('li')
print( type(li) )
print( li.text() )