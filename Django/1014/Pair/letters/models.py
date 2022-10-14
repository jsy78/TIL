from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class CustomLetters(models.Model):
    recipient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    to_email = models.CharField(max_length=30)
    from_name = models.CharField(max_length=30)
    from_email = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    garbage = models.BooleanField(default=False)
