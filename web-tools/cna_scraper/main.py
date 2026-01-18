import os
import aiohttp
import asyncio
from bs4 import BeautifulSoup

website = "https://www.channelnewsasia.com/latest-news"

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get(website) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            
            with open("cna_output.html", "w", encoding="utf-8") as f:
                f.write(html)

asyncio.run(main())