from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import operator
def accname(requests):
     return HttpResponse("Account name : Benitha")
def number(requests):
    return HttpResponse("number : 123456")
