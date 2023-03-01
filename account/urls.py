from . import views
from django.urls import path , include
from . import views 


urlpatterns = [
    path('' , views.sign_in , name='sign'),
      path('sign_up/' , views.sign_up , name='sign_up')
   
    

]