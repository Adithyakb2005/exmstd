from django.db import models

# Create your models here.
class Student(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    mark=models.IntegerField()