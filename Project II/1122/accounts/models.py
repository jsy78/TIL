from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class User(AbstractUser):
    address = models.CharField(max_length=80)
    sido = models.CharField(max_length=20)
    sigungu = models.CharField(max_length=30)
    roadname = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    profile = ProcessedImageField(
        upload_to="images/profile",
        blank=True,
        processors=[Thumbnail(100, 100)],
        format="JPEG",
        options={"quality": 95},
    )
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )

    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"
