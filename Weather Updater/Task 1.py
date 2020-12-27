import xlwings as xw
import time
import urllib, json
import urllib.request
import sys
import pytemperature as tempp
api_key='25e9b75ba4d4eb8b913970436a3b2113'
wb = xw.Book('Example.xlsx')
sht1 = wb.sheets['Weather']
sht2 = wb.sheets['City Tokens']
url_p1='http://api.openweathermap.org/data/2.5/weather?q='
url_p2='&appid='
cities=[]
count=2
while(1):
    a=sht1.range('A'+str(count)).value
    if(type(a) == type('')):
        cities.append(a)
        count=count+1
    else:
        break
while(1):
    for i in cities:
        url=url_p1+i+url_p2+api_key
        url=url.replace(' ','%20')
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        if(sht1.range('E'+str(cities.index(i)+2)).value == 1):
            if(sht1.range('D'+str(cities.index(i)+2)).value=='C'):
                sht1.range('B'+str(cities.index(i)+2)).value = tempp.k2c(data['main']['temp'])
                sht1.range('C'+str(cities.index(i)+2)).value = data['main']['humidity']
            else:
                sht1.range('B'+str(cities.index(i)+2)).value = tempp.k2f(data['main']['temp'])
                sht1.range('C'+str(cities.index(i)+2)).value = data['main']['humidity']
    time.sleep(3)
