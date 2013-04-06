from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(unique=True, max_length=100)