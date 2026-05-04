from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        context = {'city': city}
        return render(request, 'weather/index.html', {
            'context': context
        })
    return render(request, 'weather/index.html')
