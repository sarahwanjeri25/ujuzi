from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return HttpResponse("Dashboard")

def register (request):
    return HttpResponse("Register Here")