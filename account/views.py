from django.shortcuts import render
from .models import sign_in

# Create your views here.


def sign_inq(request, method = 'POST'):
    username=request.POST.get('username')
    password=request.POST.get('password')
    print(username)
    print(password)
    data = sign_in(username=username  , password=password)
    data.save()
    
    return render(request, 'sign_in.html')
    



def sign_up(request):
    return render(request, 'sign_up.html')
