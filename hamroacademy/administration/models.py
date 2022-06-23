from distutils.command.upload import upload
from django.db import models

class Company(models.Model):
    CompanyName=models.CharField(max_length=70, null=True)
    CompanyAddress=models.CharField(max_length=70)
    Logo=models.ImageField(upload_to='uploads/')
    phoneno=models.BigIntegerField(null=True)
    def __str__(self) :
        return self.CompanyName



class Course(models.Model):
    course_number = models.CharField(max_length=5, primary_key=True)
    course_name = models.CharField(max_length=40)
    max_numb_students = models.CharField(max_length=65)
    instructors = models.CharField(max_length=65)

