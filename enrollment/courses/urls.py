from django.urls import path
from . import views

urlpatterns = [
    path('course2/',views.course2,name='course2'),
    path('courses/', views.courses,name='courses'),
]

