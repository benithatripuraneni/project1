from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(requests):
    return HttpResponse('<h1>This is my page.</h1>')
def me(requests):
    return HttpResponse('<h1>I am a student.</h1>')
def hobies(requests):
    return HttpResponse('<h1>Playing badminton, Listening to Music.</h1>')

# Create your views here.
