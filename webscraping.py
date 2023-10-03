from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
base_url = "https://lol.fandom.com/"
page = requests.get("https://lol.fandom.com/wiki/World_Championship")
soup = BeautifulSoup(page.text, "html.parser")

# selecting the right data to be exctracted(ALl Worlds CHampionship Season)
all_season = soup.find_all("div", class_ = "hlist")[2].ul.find_all("li")
seasons_url = []
champion_data = []

# Extracting all the links to all Worlds Championsip data links
for season in all_season:

    season = season.a.get("href")
    seasons_url.append(season)

for url in seasons_url:
    page = requests.get("https://lol.fandom.com" + f"{url}" + "/Champion_Statistics")
    if page.status_code == 200:
        print(url,"connected")
        soup = BeautifulSoup(page.text, "html.parser")
        table = soup.find("table", class_="wikitable")
        table_columns = table.find_all("tr")[4].find_all("th")

        champ_columns = []
        for column in table_columns:

            champ_columns.append(column.text.strip())



        table_row = table.find_all("tr")[5:]

        #finding each cell in a row
        for i in table_row:
            row = i.find_all("td")
            my_list = []

            #scraping all the value in each cell in a row and saving it into a list
            for x in row:

                my_list.append(x.text.strip())
            champion_data.append(my_list)
    else:
        pass
    

df = pd.DataFrame(champion_data, columns= champ_columns)

print(df.head(10))









