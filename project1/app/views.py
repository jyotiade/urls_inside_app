from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>welcome t0 home 1</h1>")

def register(request):
    return render(request,'register.html')
    