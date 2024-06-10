from django.shortcuts import render
from classes.models import Classes

# Create your views here.
def classes(request):
    classes = Classes.objects.all().values()
    return render(request, 'classes/classes.html', {
        "classes":classes
    })