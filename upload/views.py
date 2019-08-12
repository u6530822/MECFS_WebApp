from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Upload page</h1>")

def display(request):
    return HttpResponse("<h1>Display and edit data page</h1>")

