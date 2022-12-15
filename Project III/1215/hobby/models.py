from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Categories(models.Model):
    category = models.CharField(max_length=20)

class Hobby(models.Model):
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Hobby')
    title = models.CharField(max_length=80)
    category = models.CharField(max_length=20)
    tags = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    meeting_day = models.DateTimeField()
    address_type = models.BooleanField(default=False) # False=오프라인, True=온라인
    address = models.CharField(max_length=100, default='온라인') # 온라인 or 오프라인 주소
    X = models.CharField(max_length=30, null=True, blank=True)
    Y = models.CharField(max_length=30, null=True, blank=True)
    entry_fee = models.CharField(max_length=20, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    hits = models.PositiveBigIntegerField(default=0)
    recruit_type = models.BooleanField(default=False) # 자유가입(False), 승인제(True)
    limit = models.IntegerField(default=3, validators=[MinValueValidator(3), MaxValueValidator(15)])
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Accepted')
    image = models.ImageField(
        upload_to="images/",
        blank=True,
    )
    image_thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(300, 300)],
        format="JPEG",
        options={"quality": 80},
    )
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_hobby')

class Accepted(models.Model):
    joindate = models.DateTimeField(auto_now=True)
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE, related_name='accepted')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    joined = models.BooleanField(default=False) # 승인여부

class Tag(models.Model):
    tag = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=20, null=True) 

class HobbyComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comment')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='recomment')

