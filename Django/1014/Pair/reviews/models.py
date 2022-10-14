from django.db import models
from django.contrib.auth import get_user_model  # from accounts.models import User


# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    movie_name = models.CharField(max_length=80)
    grade = models.FloatField(default=1.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
