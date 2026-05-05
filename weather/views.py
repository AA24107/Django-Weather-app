from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        req = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' +city+ '&appid=685cc9e89c1734c32384a424251c55a0').read()
        json_data = json.loads(req)
        data = {
            'country_code': str(json_data['sys']['country']),
            'city': city,
            'coordinate': str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp']),
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),
        }
        return render(request, 'weather/index.html' , {'data': data})
    return render(request, 'weather/index.html')
