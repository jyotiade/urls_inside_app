from django.urls import path
from app import views 


urlpatterns = [
    path('app/',views.home),
    # path('register/',views.register),
    path('register/',views.register),
    path('new/',views.new,name='new'),
    path('registerdata/',views.registerdata,name='new'),
   
]