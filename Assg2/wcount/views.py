from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(requests):
    return render(requests,'wcount/home.html')
def me(requests):
    return render(requests,'wcount/me.html')
def hobies(requests):
    return HttpResponse('<h1>Playing badminton, Listening to Music.</h1>')

# Create your views here.
