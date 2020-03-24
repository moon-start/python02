import asyncio
from pyppeteer import launch
 
async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://quotes.toscrape.com/js/')
    await page.screenshot(path='example.png')
    await page.pdf(path='example.pdf')
    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }''')
 
    print(dimensions)
    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
    await browser.close()
 
asyncio.get_event_loop().run_until_complete(main())


## 獲得
## https://cuiqingcai.com/6942.html
## 執行自定義的JavaScript 獲得特定的內容，代碼如下：

## 用了evaluate 方法執行了一些JavaScript，JavaScript 傳入的是一個函數，
## 使用return 方法返回了網頁的寬高、像素大小比率三個值，最後得到的是一個JSON 格式的對象，內容如下

## API 方法 查看
## https://miyakogi.github.io/pyppeteer/reference.html