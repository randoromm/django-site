from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
    return redirect('/home/')

def home(request):
    return render(request, 'portfolio/home.html')

def p5js(request):
    return render(request, 'portfolio/p5js.html')
