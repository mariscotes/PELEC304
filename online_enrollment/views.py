from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course, Schedule, Transcript, Department  
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})

def course_list(request):
    courses = Course.objects.all()
    return render(request, "course_list.html", {"courses": courses})

def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, "schedule_list.html", {"schedules": schedules})

def transcript_list(request):
    transcripts = Transcript.objects.all()
    return render(request, "transcript_list.html", {"transcripts": transcripts})

def department_list(request):
    departments = Department.objects.all()
    return render(request, "department_list.html", {"departments": departments})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form, 'item': student})

