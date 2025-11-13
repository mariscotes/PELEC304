from django.contrib import admin
from .models import TestingDatabase , Course , Schedule , Transcript ,Department , Student 

admin.site.register(TestingDatabase)
admin.site.register(Course)
admin.site.register(Schedule)
admin.site.register(Transcript)
admin.site.register(Department)
admin.site.register(Student)