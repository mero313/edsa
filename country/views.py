from django.shortcuts import render
from .models import People , Custom , Event , Food

# Create your views here.


def country(request):
    x = {'people': People.objects.all()}
    return render(request , 'country.html' , x )