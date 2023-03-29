import random
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
    next_city = ['뉴욕', '오사카', '카이로', '파리', '팀북투', '요하네스버그', '스톡홀름', '부에노스 아이레스', '아비장', '더블린', '치앙마이', '세부', '모스크바', '상파울루', '시애틀', '리스본']
    city = random.choice(next_city)
    context = {
        'city': city,
    }
    return render(request, 'cities.html', context)


