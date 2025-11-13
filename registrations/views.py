from django.shortcuts import render
from django.http import HttpResponse

def registrations(request):
    return HttpResponse('registered')

def registration(request):
    return HttpResponse('not registered')