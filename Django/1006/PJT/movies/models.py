from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    summary = models.TextField()
    running_time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
