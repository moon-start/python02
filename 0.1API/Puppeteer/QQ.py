# pip install asyncio
import asyncio
from pyppeteer import launch
from lxml import etree

from appHH import main

# url ="https://18h.animezilla.com/manga/3931/4"



import time
for  n in range(1,11):
    print(n)
    url ="https://comicbus.live/online/comic-103.html?ch=1-"+str(n)
    asyncio.get_event_loop().run_until_complete(main( url,str(n) )   )



