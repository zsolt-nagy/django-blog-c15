# Create your models here.
from django.db import models
import datetime

class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description=models.TextField()
    publish_date = models.DateField(default=datetime.date.today)

