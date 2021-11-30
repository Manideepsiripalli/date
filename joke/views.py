from django.shortcuts import render
from django.http import HttpResponse
import datetime


date1=datetime.datetime.now()


def Dateview(request):
    x="<h1> The current date and time is{}</h>".format(date1)
    return HttpResponse(x)

# Create your views here.
