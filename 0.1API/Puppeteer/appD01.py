import asyncio
from pyppeteer import launch

from pyquery import PyQuery as pq

## pip install cheerio
# import cheerio
    

################################# 這是一個 截圖 PY
pngPath = "0.1API/example.png"


# url = "https://ithelp.ithome.com.tw/ironman"
url = "https://sample.myrenta.com/viewer/sc/viewerjs/sample/9-154841-84/RTL001/index.html"

async def main():
    browser = await launch({"headless":False})
    # browser = await launch()
    # browser = await launch(devtools=True) 
    page = await browser.newPage()
    await page.goto( url )


    ## 先等待網頁載入到底下的section的html標籤，不然有時候執行太快抓不到網頁
    # await page.waitForSelector('section') ..這一段會錯誤??

  


    # 页面内容源码 ###############
    # content = await page.content()
    # # 页面会话的cookies
    # cookies = await page.cookies()
     # 打印当前页标题
    # print(await page.title()
    ##################################
    # ## 把BODY 抓出來
    # body = await page.content()
    # print(type(body))
    # f = open('./0.1API/QQ.txt', 'w',encoding="utf8")
    # f.write(body)
    # f.close()

    # ArrowLeft   #37  左
    # ArrowRight  #39  右

    ## 一直按著
    # await page.keyboard.down('ArrowLeft')
    # await page.keyboard.press('ArrowLeft')



    # print(ele)
    # eaa = await page.xpath('//*[@id="Viewer"]')  ## list  ## //*[@id="Viewer"]/div[3]/div[1]
    # eaa = await page.xpath('//*[@class="readerCanvas"]')  ## list  
    # print(eaa)
    # for item in eaa:
    #     ## position: fixed; width: 100%; opacity: 1;
    #     # title_link = await (await item.getProperty('style')).jsonValue()
    #     title_link = await (await item.getProperty('id')).jsonValue()
    ##
        # title_link = await (await item.getProperty('class')).jsonValue()
        # print(title_link)

    # eaa = await page.xpath('//*[@id="Viewer"]/div[3]/div[1]/div/div/img[1]')
    # print(eaa)
    # # //*[@id="Viewer"]/div[3]/div[1]/div/div/img[1]
    # for item in eaa:
    #     title_link = await (await item.getProperty('class')).jsonValue()
    #     print(title_link)
        # 获取文本
        # title_str = await (await item.getProperty('textContent')).jsonValue()
        # print(await item.getProperty('textContent'))
        # 获取链接
        # title_link = await (await item.getProperty('href')).jsonValue()
        # print(title_str)
        # print(title_link)
 

    # >cheerio.cheerio ()
    ##QQ  = await cheerio.cheerio(body)
    # cheerio.load(body)

    # await page.screenshot({'path': pngPath })

    await asyncio.sleep(100)  ##  不關閉
    # await browser.close()     ##  關閉

asyncio.get_event_loop().run_until_complete(main())




   # 设置页面视图大小 ......................................................沒效果?
    # await page.setViewport(viewport={'width':1280, 'height':800})
    # 是否启用JS，enabled设为False，则无渲染效果
    # await page.setJavaScriptEnabled(enabled=True)
