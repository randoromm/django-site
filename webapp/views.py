from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Test test test :O!</h2>")

# Create your views here.
