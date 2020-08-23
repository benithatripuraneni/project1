from django.shortcuts import render
import operator
from django.http import HttpResponse

def home(requests):
       return render(requests, 'vremove/home.html')
def count(requests):
       mytext=requests.GET['fulltext']
       v= ('a','e','i' ,'o','u', 'A','E','I','O','U')
       count=0
       for x in mytext:
             if x in v:
                 mytext= mytext.replace(x, "")
                 count=count +1
       return render(requests, 'vremove/count.html', {'mycount':count, 'yourtext':mytext})
# Create your views here.
