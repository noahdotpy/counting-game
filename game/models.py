from django.db import models

# Create your models here.
class Clicker(models.Model):
    clicks = models.IntegerField(default=0)