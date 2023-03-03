from . import views
from django.urls import path , include
from . import views 

urlpatterns = [
     path('' , views.country1 , name='country1' ),
    path('<int:id>' , views.country_id , name='country_id'),
    
    
   
]
