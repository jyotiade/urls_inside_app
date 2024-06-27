from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse

def home(request):
    #  return HttpResponse("<h1 style=color:lightpink>welcome t0 home 3</h1>")

    data={"name":"viti","age":"20","quali":"b.tech"}
    return JsonResponse(data)