from django.db import models

# Create your models here.
class Classes(models.Model):
    name = models.CharField(max_length=250)
    teacher = models.CharField(max_length=250)
    duration = models.IntegerField()
    students = models.IntegerField()