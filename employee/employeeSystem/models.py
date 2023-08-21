from pyexpat import model
from django.db import models
import datetime

# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class registration(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.CharField(max_length=40)

class feedback(models.Model):
    userfeedback = models.CharField(max_length=255)
    username = models.CharField(max_length=50)

class messages(models.Model):
    message = models.CharField(max_length=255)
    username = models.CharField(max_length=50)

class userattendence(models.Model):
    attendence = models.CharField(max_length=50)
    username  = models.CharField(max_length=50)

class task(models.Model):
    taskname = models.CharField(max_length=50)
    usermail = models.CharField(max_length=50)
    starttime = models.DateField()
    endtime = models.DateField()

    



    # def __str__(self):
    #     return self.firstname

    # @staticmethod
    # def getemail(email):
    #     try:
    #         return registration.objects.get(email=email)
    #     except:
    #         return False