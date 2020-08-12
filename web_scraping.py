#libraries like beautiful soup and requests
#pip install beautifulsoup4
#pip install requests
#pip install pandas
import pandas as pd
import requests
from bs4 import BeautifulSoup

page=requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05361000000005&lon=-118.24549999999999#.Xx036_kzbIU')
soup = BeautifulSoup(page.content,'html.parser')#to find html tages
#print(soup.find_all('a'))
week = soup.find(id='seven-day-forecast-body')
#print(week)
#print(week.find_all('li'))
items = week.find_all(class_='tombstone-container')
#print(items[0])
#print(items[0].find(class_='period-name').get_text())
#print(items[0].find(class_='short-desc').get_text())
#print(items[0].find(class_='temp').get_text())
period_name=[item.find(class_='period-name').get_text() for item in items]
#print(period_name)
short_desc=[item.find(class_='short-desc').get_text() for item in items]
#print(short_desc)
temperatures=[item.find(class_='temp').get_text() for item in items]
#print(temp)

weather_stuff=pd.DataFrame(
    {
        'periods':period_name,
        'short_desc':short_desc,
        'temp':temperatures
    })
print(weather_stuff)
weather_stuff.to_csv('weather.csv')
