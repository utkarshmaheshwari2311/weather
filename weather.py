import requests
api_address = 'http://api.openweathermap.org/data/2.5/weather?'
ident = '&appid=4a369a065de8228621bc21e706654d81'
city = input("City name: ")
url = api_address + 'q=' + city + ident
json_data = requests.get(url).json()
print(json_data)