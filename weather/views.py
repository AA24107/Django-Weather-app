from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        try:
            req = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' +city+ '&appid=685cc9e89c1734c32384a424251c55a0').read()
            json_data = json.loads(req)
        except:
            return render(request, 'weather/index.html', {'error': 'City not found'})
        temp = json_data['main']['temp'] - 273.15
        data = {
            'country_code': str(json_data['sys']['country']),
            'city': city,
            'description': str(json_data['weather'][0]['description']),
            'coordinate': str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            'temp': str(round(temp, 2)) + ' °C',
            'pressure': str(json_data['main']['pressure']) + ' hPa',
            'humidity': str(json_data['main']['humidity']) + ' %',
        }
        return render(request, 'weather/index.html' , {'data': data})
    return render(request, 'weather/index.html')
