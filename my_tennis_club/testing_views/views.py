from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def hello_world(request):
    return HttpResponse("Hello From Function-Based View!")

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello From Class-Based View!")
    
    def student_profile(request):
        student = {"name": "Juan Dela Cruz", "age":21 , "course":"BSIT"}

        return render(request , 'student_profile.html', {"student":student})

   
        
