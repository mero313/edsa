from django.shortcuts import render
from .models import People, Custom, Event, Food

# Create your views here.


def country1(request):
    x = {'people': People.objects.all()}
    return render(request, 'country1.html', x)


def country(request):
    y = {'people': People.objects.all()}
    return render(request, 'country.html', y)


def country_id(request, id):
    x = {'event': Event.objects.get(people_id=People.objects.get(id=id)),
         'people': People.objects.get(id=id), }
    return render(request, 'country_id.html', x)
