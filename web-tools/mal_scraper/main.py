import os
import pandas as pd
import random
import aiohttp
import asyncio
from bs4 import BeautifulSoup

from extract import get_anime_details

# Get .csv file
os.chdir(os.getcwd() + "/mal_scraper/")
# print(f"Current directory: {curr_dir}\n")

csv_file = "anime_no_start_airing_date.csv"
df = pd.read_csv(csv_file)
# print(f"Column headers: {list(df.columns)}\n")

mal_urls = df["mal"]

# Header variables for aiohttp
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://myanimelist.net/' # Important: Pretend we came from the main page
}

# Get html information from each link
async def get_html_info(headers, urls):
    async with aiohttp.ClientSession(headers=headers) as session:
        row = 0

        for url in urls:
            try:
                async with session.get(url, timeout=15) as response:
                    if response.status == 200:
                        html = await response.text()                        
                        soup = BeautifulSoup(html, "html.parser")
                        
                        anime_data = get_anime_details(soup)
                        # print(f"URL:         {url}")
                        # print(f"Title:       {anime_data[0]}")
                        # print(f"Episodes:    {anime_data[1]}")
                        # print(f"Airing Date: {anime_data[2]}\n")

                        await asyncio.sleep(random.uniform(2, 5)) # Sleep randomly between 2 to 7 seconds

                        # Update .csv column 'started_airing'
                        print(f"({row}) Updating '{anime_data[0]}'...\n")
                        airing_start_date = anime_data[2]
                        column = "started_airing"
                        df.loc[row, column] = ""
                        df.loc[row, column] = airing_start_date

                    elif response.status == 403:
                        print("⛔ Access Denied (403).\n")
                        return None

                    else:
                        print(f"❌ Error Status: {response.status}\n")
                        return None
            
            except Exception as error:
                print(f"❌ Connection Error: {error}\n")

            row += 1
    
    return None

asyncio.run(get_html_info(headers, mal_urls))

df.to_csv(csv_file, index=False)
print("Code has finished running.\n")