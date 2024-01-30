from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_star_systems_within_75%E2%80%9380_light-years"

# Webdriver
browser = webdriver.Chrome()
browser.get(START_URL)

time.sleep(10)

planets_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

        ## ADD CODE HERE ##
        soup = BeautifulSoup(browser.page_source,"html.parser")
        table = soup.find_all("table",attrs={"class","wikitable sortable jquery-tablesorter"})
        trs=table.find_all("tr")
        for tr in trs:
            litags = tr.find_all("td")
            temp = []
            for index,litag in enumerate(litags):
                #print(litag.contents[0])
                    try:
                        temp.append(litag.contents[0])
                    except:
                        temp.append("")        
            planets_data.append(temp)
    




        
# Calling Method    
scrape()
#print(planets_data)

# Define Header
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Define pandas DataFrame   
planets_df = pd.DataFrame(planets_data,columns=headers)

# Convert to CSV
planets_df.to_csv("scrapped_data1.csv",index=True,index_label="id")
    


