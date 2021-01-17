# In this simple Scraping project We are going to scrape a Simple weather forecast site using BeautifulSoup. We will scrape All information related to weather i.e, Temperature, its description and most importantly day

# Importing Few libraries to start projetc
import requests     # To access web URL
import pandas as pd     # To convert all the collected data into pandas dataframe for data analysis
from bs4 import BeautifulSoup   # To create soup objects and enables much more functions

# First we need to access the webpage which we want to scrape.
req = requests.get("https://forecast.weather.gov/MapClick.php?lat=38.890370000000075&lon=-77.03195999999997#.YAG7gOgzZPY")

# Creating Soup object of accessed URL
soup = BeautifulSoup(req.content, "html.parser")

# We need to store parent class of all required scrape info in a variable
items = soup.find_all(class_ = "tombstone-container")

# Accessing each information individually
periodName = [item.find(class_ = "period-name").get_text() for item in items]
descShort = [item.find(class_ = "short-desc").get_text() for item in items]
highTemp = [item.find(class_ = "temp").get_text() for item in items]

'''
print(periodName)
print(descShort)
print(highTemp)
'''

# Converting collected data into dataframes
df= pd.DataFrame({
    "Periods Name" : periodName,
    "Short Description" : descShort,
    "Temperature" : highTemp
})
print(df)
