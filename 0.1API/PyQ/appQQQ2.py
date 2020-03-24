# import asyncio
# from pyppeteer import launch
 
# async def main():
#     await launch(headless=False)
#     await asyncio.sleep(100)
 
# asyncio.get_event_loop().run_until_complete(main())
###############
import asyncio
from pyppeteer import launch
 
# async def main():
#     browser = await launch(devtools=True)    ## 檢查模式
#     # browser = await launch(headless=False, args=['--disable-infobars'])
#     page = await browser.newPage()
#     await page.goto('https://www.google.com')
#     await asyncio.sleep(100)
 
# asyncio.get_event_loop().run_until_complete(main())


## 檢查模式
 

width, height = 1366, 768

async def main():
    browser = await launch(headless=False, userDataDir='./userdata', args=[f'--window-size={width},{height}'] )  ## 增加   args=[f'--window-size={width},{height}']
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})                         ## 增加
    await page.goto('https://www.taobao.com')
    await asyncio.sleep(100)
 
asyncio.get_event_loop().run_until_complete(main())

