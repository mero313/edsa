from . import views
from django.urls import path , include
from . import views 

urlpatterns = [
    path('' , views.country , name='country'),
   
]
