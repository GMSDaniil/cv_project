from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length=100)
    date = models.TimeField()