import os
from bs4 import BeautifulSoup

project_path = os.getcwd() + '/hnk-python-tools/web-tools/cna_scraper/'

with open(project_path + 'cna_latest_news.html', 'r', encoding='utf-8') as file:
    html_cont = file.read()

soup = BeautifulSoup(html_cont, 'html.parser')


# class = "quick-link quick-link--list-object" 
#   attributes
#       data-category
#       data-heading
#       data-link_absolute

categories = ["Singapore", "Asia", "East Asia", "World", "Business"]

tags = soup.find_all(attrs={"data-category": categories})

i = 1
with open(project_path + "news_i_want.txt", "w", encoding="utf-8") as f:
    for tag in tags:
        
        category = tag["data-category"]
        link = tag["data-link_absolute"]
        title = tag["data-heading"]

        f.write(f"{i}\n")
        f.write(f"Category: {category}\n")
        f.write(f"Title: {title}\n")
        f.write(f"Link: {link}\n\n")
        
        i += 1

# To do
# Sort news by category


print("--- END ---")