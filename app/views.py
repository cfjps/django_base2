from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>My web page number 1</h1>')