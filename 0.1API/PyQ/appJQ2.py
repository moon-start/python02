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



## 屬性操作
# ## .attr()  修改
# p = pq('<p id="hello" class="helloB"></p>')('p')
# print( p.attr("id") )              ## 傳回內容
# print( p.attr("class") )           ## 傳回內容
# print( p.attr("id", "plop") )
# print( p.attr("id", "hello") )


# p = pq('<p id="hello" class="hello"></p>')('p')
# print( p.addClass('beauty')   )      ## 新增 class 內容
# print( p.removeClass('hello')   )    ## 刪除 class 內容
# print( p.css('font-size', '16px')   )               ## 新增  ('屬性','內容')           ## 2參數 字串
# print( p.css({'background-color': 'yellow'})   )    ## 新增  ({ '屬性':'內容')  })     ## 1參數 集合
    

## DOM 操作
p = pq('<p id="hello" class="hello"></p>')('p')
print( p.append(' check out <a href="http://reddit.com/r/python"><span>reddit</span></a>')  )   ## 寫入元素標籤中  的內容
print( p.prepend('Oh yes!')  )                                                                  ## 寫入元素標籤中  的內容 
print( p.append(' check outＡＢＣ')  )   ## 寫入元素標籤中  的內容

print('###'*20)
d = pq('<div class="wrap"><div id="test"><a href="http://cuiqingcai.com">Germy</a></div></div>')  
p.prependTo(d('#test'))   ## 在d變數中的 #test標籤的內容..放入 p變數的內容
print(p)  ## 還是原來的
print(d)

print('###'*20)
d.empty()  ## 清空 只保留 root標籤
print(d)