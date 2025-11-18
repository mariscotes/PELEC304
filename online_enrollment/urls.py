from django.urls import path
from . import views

urlpatterns = [
   path('courses/',views.course_list,name='curse'),
   path('students/',views.student_list,name='student_list'),
   path('transcript/',views.transcript_list,name='transcript'),
   path('dept/',views.department_list,name='department'),
   path('sched/',views.schedule_list,name='schedule'),
   path('add/',views.add_student,name='add_student'),
   path('edit/<int:pk>/', views.edit_item, name='edit'),
]

