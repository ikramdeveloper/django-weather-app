from django.shortcuts import render
import json
import urllib.request
import environ
import os

env = environ.Env()

environ.Env.read_env(os.path.join('../project', '.env'))

APP_KEY = env('WEATHER_API_KEY')


# Create your views here.
def home(request):
    if(request.method == 'POST'):
        city = request.POST['city']
        weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APP_KEY}'
        weather_url = weather_url.replace(' ', '%20')
        res = urllib.request.urlopen(weather_url).read()
        json_data = json.loads(res)
        data = {
            'country_code': json_data['sys']['country'],
            'coordinate': str(json_data['coord']['lat']) + ' lat, ' + str(json_data['coord']['lon']) + ' lon',
            'temp': json_data['main']['temp'],
            'pressure': json_data['main']['pressure'],
            'humidity': json_data['main']['humidity']
        }
    else:
        city = ''
        data = {}

    context = {'city': city, 'data': data}
    return render(request, 'index.html', context)
