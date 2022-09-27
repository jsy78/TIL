from pyexpat import model
from django.db import models


class Todo(models.Model):
    content = models.CharField(max_length=80)
    priority = models.IntegerField()
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
