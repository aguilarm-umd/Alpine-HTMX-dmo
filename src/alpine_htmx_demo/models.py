from django.db import models

# Create your models here.

class TodoModel(models.Model):
    todo = models.CharField(max_length=255)
    counter = models.BigIntegerField()
