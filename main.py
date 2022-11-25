import os
import requests
import webbrowser
from keep_alive import keep_alive
import scratchattach as scratch3

keep_alive()

API_KEY = os.environ['API_key']
sessionID = os.environ['sessionID']
session = scratch3.Session(sessionID , username="LoIdesMio")
conn = session.connect_cloud("764555125")
client = scratch3.CloudRequests(conn)
dc_weather = []
webbrowser.open_new_tab('https://scratch.mit.edu/projects/764555125/editor/')
@client.request
def get_weather(argument1):
  print(argument1)
  webbrowser. open('https://scratch.mit.edu/projects/764555125/editor/')
  print("Got request")
  url = 'https://api.openweathermap.org/data/2.5/weather?q='+ argument1 +'&appid=' + API_KEY
  weath = requests.get(url)
  print(weath)
  js = weath.json()
  print('jsoneddd')
  print(js)
  if js['cod'] == 200:
   weather = js['weather'][0]['main']
   weather_desc = js['weather'][0]['description']
   temp  = js['main']['temp']
   feel_temp = js['main']['feels_like']
   min_temp = js['main']['temp_min']
   max_temp = js['main']['temp_max']
   icon_id = js['weather'][0]['icon']
   country = js['sys']['country']
   wind_speed = js['wind']['speed']
   humidity = js['main']['humidity']
   weather_list = [weather , weather_desc , temp , feel_temp , min_temp, max_temp , icon_id , country , wind_speed , humidity]
   return weather_list
  elif js['cod'] == '404':
     return 'NOT FOUND'
  elif js['cod'] == '429':
    return 'WAIT'



client.run()
