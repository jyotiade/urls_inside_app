from django.db import models

# Create your models here.
#table related work

class Student(models.Model):
    Name=models.CharField(max_length=50)  #var1
    Email=models.EmailField()             #var2
    Contact=models.IntegerField()         #var3
    Password=models.IntegerField(null=True)
