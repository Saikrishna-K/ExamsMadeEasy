from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
# Create your models here.


# Contains examination details
class ExamDetails(models.Model):
    examiner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(primary_key=True,max_length=50)
    about = models.CharField(max_length=1000)
    qCount = models.IntegerField()
    total = models.IntegerField()
    duration = models.IntegerField()



# Contains Questions ,Options,Correct answer
class Questions(models.Model):
    exam = models.ForeignKey(ExamDetails, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct = models.IntegerField()


# Contains Result of the attempted Exam per User
class Result(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(ExamDetails, on_delete=models.CASCADE)
    marks = models.IntegerField()
    attempt_time = models.CharField(max_length=20)
