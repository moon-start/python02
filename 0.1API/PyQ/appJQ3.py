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



## 走訪
from pyquery import PyQuery as pq

## 文件
doc = pq(filename='./0.1API/hello.html')

## 把 li元素的內容  列印
lis = doc('li')
for li in lis.items():
    print( li.html() )

print('###'*20)
print( lis.each(lambda e: e)  )


# ## 網頁請求
# print( pq('http://cuiqingcai.com/', headers={'user-agent': 'pyquery'}) )
# print( pq('http://httpbin.org/post', {'foo': 'bar'}, method='post', verify=True) )