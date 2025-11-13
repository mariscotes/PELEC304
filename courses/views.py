from django.shortcuts import render 
from django.http import HttpResponse

def courses(request):
    return HttpResponse('IT')

def course2(request):
    return HttpResponse('BISAIS')

# Create your views here.
