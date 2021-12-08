from django.db import models


class Visit(models.Model):
    visitor = models.CharField(max_length=100)
    reason = models.CharField(max_length=140)
    date_time = models.DateTimeField()


class StudentModel(models.Model):
    name = models.CharField(max_length=30)
    grades = models.CharField(max_length=300)
    average_grades = models.FloatField()
