from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#recursive-relationships
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.ManyToManyField.symmetrical
    # A가 B를 팔로잉, 이 것은 서로 친구 X(symmetrical=False)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    
    @property
    def full_name(self):
        return f'{self.last_name}{self.first_name}'