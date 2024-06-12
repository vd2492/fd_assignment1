# app1/models.py

from django.db import models

class StudentRegistration(models.Model):
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name
