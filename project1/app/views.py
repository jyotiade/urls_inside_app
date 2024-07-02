from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("<h1>welcome t0 home 1</h1>")

def register(request):
    return render(request,'register.html')

def home(request):
    return redirect("https://www.jiocinema.com/")

def new(request):
    return render(request,'new.html')

def registerdata(request):
    print(request.method)
    print(request.POST)
    
    name=request.POST.get('name')
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    print(name,email,contact)