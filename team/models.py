# team/models.py
from django.db import models

class Teammate(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    resume = models.TextField()  # You can also use a FileField if you have a file

    def __str__(self):
        return self.name
