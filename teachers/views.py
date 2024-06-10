from django.shortcuts import render
from teachers.models import Teachers

# Create your views here.
def teachers(request):
    teachers = Teachers.objects.all().values()
    return render(request, 'teachers/teachers.html', {
        "teachers":teachers
    })