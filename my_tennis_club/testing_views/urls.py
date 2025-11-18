from django.urls import path
from . import views

urlpatterns = [
    path('student_profile/', views.student_profile, name="student profile"),
    path('student_list/', views.student_list, name="student list"),
    path('fbv/', views.hello_world, name="Function-based"),
    path('cbv/', views.HelloWorldView.as_view(), name="Class-Based")
]