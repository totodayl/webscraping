from bs4 import BeautifulSoup
import requests
import pandas as pd

base_url = "https://lol.fandom.com/"
page = requests.get("https://lol.fandom.com/wiki/World_Championship")
soup = BeautifulSoup(page.text, "html.parser")

# selecting the right data to be exctracted(ALl Worlds CHampionship Season)
all_season = soup.find_all("div", class_ = "hlist")[2].ul.find_all("li")
seasons_url = []
print(all_season)

# Extracting all the links to all Worlds Championsip data links
for season in all_season:

    season = season.a.get("href")
    seasons_url.append(season)

for url in seasons_url:
    page = requests.get("https://lol.fandom.com" + "/Season_3_World_Championship" + "/Champion_Statistics")
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, "html.parser")

        table = soup.find("table", class_="sortable")
        table_row = table.find_all("tr")[5:]
        for x in table_row:
            if x.find(attrs={'title': True}):
                print()
            else:
                pass





