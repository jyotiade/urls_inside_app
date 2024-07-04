from django.urls import path
from app2 import views 


urlpatterns = [
    path('app2/',views.home),
    path('form/',views.form),
    path('homes/',views.homes,name='homes')
]