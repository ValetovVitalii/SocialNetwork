from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request): #HttpRequest
    return HttpResponse("music қосымшасының беті.")

def categories(request,cat_id): #HttpRequest
    return HttpResponse("<h1>Категориялар бойынша мақалалар</h1><p>id: {cat_id}</p>")

