from django.shortcuts import render
from django.http import HttpResponse
from . import views

# to render the html files 
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
# Create your views here.
