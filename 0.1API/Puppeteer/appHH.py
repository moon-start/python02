
import asyncio
from pyppeteer import launch
from lxml import etree


## 下載圖片用
## pip install aiohttp
# import aiohttp
# ############### 放入圖片網址 ######################   
# async with aiohttp.ClientSession() as session:
#     response =await session.get( RR )
#     content = await response.read()
# with open('A.jpg', 'wb') as f:
#     f.write(content)
# print('下载第 1張圖 成功')
######################
import requests



from pyquery import PyQuery as pq

## pip install cheerio
# import cheerio
    

################################# 這是一個 截圖 PY
pngPath = "0.1API/example.png"


# url = "https://ithelp.ithome.com.tw/ironman"
# url = "https://sample.myrenta.com/viewer/sc/viewerjs/sample/9-154841-84/RTL001/index.html"

# url ="https://18h.animezilla.com/manga/3931/4"
url = "https://comicbus.live/online/comic-103.html?ch=1-3"
n = "1"


# global ww,hh,uu


async def main(url,n):
    print(url)

    global RR,ww,hh
    ww,hh = 1366,768
    ## chrome 的 版面
    browser = await launch({"headless":True})                                     ## 不顯示
    # browser = await launch(headless=False, args=[f'--window-size={ww},{hh}'] )  ## 顯示
    ## html 的 版面   
    page = await browser.newPage()
    await page.setViewport({'width': ww, 'height': hh}) 
    ######################################################


    # print(RR)

 
    await page.goto( url )


    ## 一份 HTML 文件
    pq( await page.content() )
  
    ## 向下滾動
    # await page.evaluate('_ => {window.scrollBy(0, window.innerHeight);}')  
    ##############################################
    ## 取得 
    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }''')  # 执行js代码
    print(dimensions)  # 返回js执行结果
    #################################################### 以下是JS傳回 然後設定BODY 寬高
    # ## () => {  return {) }
    # dimensions = await page.evaluate('''() => {
    # return {
    #         width: window.screen.availWidth,
    #         height: window.screen.availHeight
    # }
    # }''')  # 执行js代码
    # print(dimensions)  # 返回js执行结果
    # ## 將頁面設定寬高 ## 將 body設定 寬高
    # await page.setViewport( dimensions )
    ####################################################



    # await page.waitForSelector('section') 
    doc = pq(  await page.content() )
    # await page.waitFor(10000)   ## 等待10秒
    print( doc('img#comic').attr("src")  )
    # print( doc('img#comic').attr("wi") )
   


   
    ## 導向
    # await page.goto( doc('body img#comic').attr("src") )  
    # await page.goto( doc('body img[id=comic]').attr("src") )        ## 屬性選擇
    # await page.goto( doc('body a > p > img[id=comic]').attr("src") )  ## 指定選擇
    

    # ## 本文 --------page 記錄著目前的頁面
    # doc = pq( await page.content() )
    # # print( doc('body > img').attr("width")  )
    # # print( doc('body > img').attr("height")  )

    # ww,hh,uu = doc('body > img').attr("width"),doc('body > img').attr("height"),doc('body > img').attr("src")
    # print(ww ," ",hh," ",uu)
    # xx,yy = doc('body > img').attr("Left"),doc('body > img').attr("Top")
    # print(xx ," ",yy)



    # await browser.close()     ##  關閉

    # print(uu)
    # RR=uu
    # print(RR)


    # ## 截圖  
    Path = "0.1API/Puppeteer/PNG/"
    await page.screenshot({'path': Path + "example-"+n+".png" })    
    ##################################################
    # r=requests.get( RR )
    # with open(Path+'AA.jpg','wb') as f:
    #     #將圖片下載下來
    #     f.write(r.content)
    ######## 還是很小張




    # print(html.xpath('//div[@class="quote"]'))
    # eaa = await page.xpath('//*[@id="comic"]').html()
    # print(eaa)

    # ArrowLeft   #37  左
    # ArrowRight  #39  右

    ## 一直按著
    # await page.keyboard.down('ArrowLeft')
    # await page.keyboard.press('ArrowLeft')

    # await asyncio.sleep(100)  ##  不關閉
    await browser.close()     ##  關閉

# print("第一次")
# asyncio.get_event_loop().run_until_complete(main( url,n ))
# print("結束")
# print(RR," ",ww," ",hh)
###########################################################
###########################################################
###########################################################
###########################################################
###########################################################
###########################################################



# async def mainB():
#     print(type(ww))
#     wwa,hha = int(ww),int(hh)
#     # ww=int(ww)
#     # hh=int(hh)
#     ## chrome 的 版面
#     browser = await launch(headless=False, args=[f'--window-size={wwa},{hha}'] )  ## 這一行是 打開一個頁面
#     ## html 的 版面   
#     page = await browser.newPage()
#     await page.setViewport({'width': wwa, 'height': hha}) 
#     ######################################################
#     ##
#     ## 頁面
#     await page.goto( RR )
#     ##
#     ## html
#     html = pq(  await page.content() )
#     # html("body > img").attr("width" ,str(wwa))
#     # html("body > img").attr("height",str(hha))
#     # html("body > img").attr("width" ,"500")
#     # html("body > img").attr("height","500")


#     ##
#     ## 屬性修改
#     ## 屬性操作
# # ## .attr()  修改
# # p = pq('<p id="hello" class="helloB"></p>')('p')
# # print( p.attr("id") )              ## 傳回內容
# # print( p.attr("class") )           ## 傳回內容
# # print( p.attr("id", "plop") )
# # print( p.attr("id", "hello") )



#     dimensions = await page.evaluate('''() => {
#         var img= document.getElementsByTagName('imd')[0];
#         //var html= document.getElementsByClassName("QQ")[0];
#         //var html= document.getElementsById("QQ");
        
#         //img.style.width  = 500+'px';
#         //img.style.height = 500+'px';

#     }''')  # 执行js代码
#     # print(dimensions)  # 返回js执行结果
#     ## 將頁面設定寬高 ## 將 body設定 寬高
#     # await page.setViewport( dimensions )


#     await asyncio.sleep(100)  ##  不關閉

# # asyncio.get_event_loop().run_until_complete(mainB())