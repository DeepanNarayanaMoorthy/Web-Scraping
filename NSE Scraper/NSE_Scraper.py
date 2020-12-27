import requests
import json
import pandas as pd

# WHEN THIS CODE IS EXECUTED, 5 FILES WILL BE GENERATED IN THE DIRECTORY WHERE THIS FILE EXISTS

# USE THIS URL FOR EXTRACTING USING EQUITIES , ENTER THE SYMBOL YOU WANT AFTER 'symbols='
# https://www.nseindia.com/api/option-chain-equities?symbol=BATAINDIA

# USE THIS URL FOR EXTRACTING USING INDICES , ENTER THE SYMBOL YOU WANT AFTER 'symbols='
# https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY

new_url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'

# THIS COOKIE CHANGES EVERYDAY FOR THE WEBSITE , SO IT HAS TO BE GOT FROM THE WEBSITE EVERYDAY FOR ONLY ONE TIME, THEN THE CODE WILL WORK FOR A WHOLE DAY

cookie='_ga=GA1.2.308873587.1598006799; _gid=GA1.2.844907758.1600333752; RT="z=1&dm=nseindia.com&si=5aed2852-f16c-42e7-a52c-1c7795b224c3&ss=kf6wyizb&sl=0&tt=0&bcn=%2F%2F684fc537.akstat.io%2F&ul=xedj&hd=xee3"; ak_bmsc=739A8D8453BD40E14C61110C0DDBB586312C835451390000AC61645FE62D655A~plKOBxrTEHsqskwKYjkX4AajKSj4oc0K0R9DIK93sr1+EDgMDjTQefl/OOFUo1FGzjMt8Dkb19SOlA76cNgmndrzZD3O1UWHF92AD+BnYF+f9qYXA86yPsp86y5O3s9+q1EYQxIWYz3p1otw/gfFgBnl4XTVk31++j9lXoZtO5wTex+m6gia5MeTACGKlAHFjHhMgsk6JVzUt7tisxnyhib+mhXw4pJS8glF5DgWVuTVU='
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36','cookie' : cookie }
page = requests.get(new_url,headers=headers)
data = json.loads(page.text)


try:
    df_rec_ce = pd.DataFrame(columns = list(data['records']['data'][0]['PE'].keys())) 
    df_rec_pe = pd.DataFrame(columns =  list(data['records']['data'][0]['PE'].keys()))
except:
    df_rec_ce = pd.DataFrame(columns = list(data['records']['data'][0]['CE'].keys())) 
    df_rec_pe = pd.DataFrame(columns =  list(data['records']['data'][0]['CE'].keys()))
for i in data['records']['data']:
  try:
    df_rec_ce = df_rec_ce.append(i['CE'], ignore_index = True)
  except:
    pass
  try:
    df_rec_pe = df_rec_pe.append(i['PE'], ignore_index = True)
  except:
    pass


try:
    df_fil_ce = pd.DataFrame(columns = list(data['filtered']['data'][0]['CE'].keys())) 
    df_fil_pe = pd.DataFrame(columns =  list(data['filtered']['data'][0]['CE'].keys()))
except:
    df_fil_ce = pd.DataFrame(columns = list(data['filtered']['data'][0]['PE'].keys())) 
    df_fil_pe = pd.DataFrame(columns =  list(data['filtered']['data'][0]['PE'].keys()))
for i in data['filtered']['data']:
  try:
    df_fil_ce = df_fil_ce.append(i['CE'], ignore_index = True)
  except:
    pass
  try:
    df_fil_pe = df_fil_pe.append(i['PE'], ignore_index = True)
  except:
    pass

data['filtered'].pop('data')
data['records'].pop('data')

df_fil_ce.to_csv('filtered_CE.csv',index=False)
df_fil_pe.to_csv('filtered_PE.csv',index=False)
df_rec_ce.to_csv('records_CE.csv',index=False)
df_rec_pe.to_csv('records_PE.csv',index=False)


with open("other_info.json", "w") as outfile:  
    json.dump(data, outfile)
