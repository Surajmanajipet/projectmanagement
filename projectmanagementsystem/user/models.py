from django.db import models

# Create your models here.

class User(models.Model):
    fullname = models.CharField(max_length=150)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)  # store hashed password

    def __str__(self):
        return self.username