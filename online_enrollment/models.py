from django.db import models

class TestingDatabase(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}"
    
class Course(models.Model):
    course_id = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    credits = models.IntegerField()
    depertment = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course_id}"

class Schedule(models.Model):
    schedule_id = models.CharField(max_length=100)
    course_id = models.CharField(max_length=100)
    instructor_id = models.IntegerField()
    day = models.CharField()
    time = models.CharField()

    def __str__(self):
        return f"{self.schedule_id}"

class Transcript(models.Model):
    transcript_id = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    course_id = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    date_issued = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.transcript_id}"

class Department(models.Model):
    department_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    head_of_department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.department_id}"

class Student(models.Model):
    student_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student_id}"