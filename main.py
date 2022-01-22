import requests
import datetime

my_lat = 16.524
my_long = -88.554

parameters = {
    'lat': my_lat,
    'lng': my_long,
    'formatted': 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data['results']['sunset']
sunrise_hour = sunrise.split('T')[1].split(':')[0]
sunset_hour = sunset.split('T')[1].split(':')[0]
#print(sunrise)
# La respuesta esta en este formato:
# 2022-01-22T23:46:33+00:00
# Para obtener la hora de este resultado dividimos el string
#sunrise_hour = sunrise.split('T')[1].split(':')[0]
#print(sunrise_hour)

time_now = datetime.datetime.now()

