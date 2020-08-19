from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import operator
def drinks(requests):
     return HttpResponse(" Drinks is good for health")
def foods(requests):
    return HttpResponse("Eat healthy food")
