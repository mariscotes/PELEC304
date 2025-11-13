from django.urls import path
from . import views

urlpatterns =[
    path('student/',views.student,name='student'),
    path('student2/',views.student,name='student'),
]