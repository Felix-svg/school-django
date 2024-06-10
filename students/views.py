from django.shortcuts import render
from students.models import Students

# Create your views here.
def students(request):
    students = Students.objects.all().values()
    return render(request, 'students/students.html',{
        "students": students
    })