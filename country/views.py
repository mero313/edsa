from django.shortcuts import render
from .models import People , Custom , Event , Food

# Create your views here.


def country(request):
    return render(request , 'country.html' , {'people': People.objects.all()})