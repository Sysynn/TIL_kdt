from django.shortcuts import render

# Create your views here.
def throw(request):
    return render(request, 'throw.html')

def catch(request):
    data = request.GET.get('message')
    context = {
        'data': data,
    }
    return render(request, 'catch.html', context)

def cities(request):
    return render(request, 'cities.html')