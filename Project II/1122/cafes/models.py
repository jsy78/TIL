from django.db import models
from froala_editor.fields import FroalaField
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime, timedelta
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    sido = models.CharField(max_length=20)
    sigungu = models.CharField(max_length=30)
    roadname = models.CharField(max_length=20)
    number = PhoneNumberField(blank=True)
    opening_hour = models.CharField(max_length=40)
    menu = FroalaField(
        options={
            "toolbarSticky": False,
            "heightMin": 200,
        }
    )
    menuStripTag = models.TextField(default="", blank=True, null=True)
    parking = models.CharField(max_length=20)
    dayoff = models.CharField(max_length=20)
    category = (
        ("분위기가 좋은", "분위기가 좋은"),
        ("디저트가 맛있는", "디저트가 맛있는"),
        ("커피가 맛있는", "커피가 맛있는"),
        ("작업하기 좋은", "작업하기 좋은"),
        ("커피가 저렴한", "커피가 저렴한"),
        ("이색적인", "이색적인"),
    )
    cafeType = models.CharField(max_length=20, choices=category, null=True)
    image1 = ProcessedImageField(
        upload_to="images/cafe",
        blank=False,
        processors=[ResizeToFill(1200, 760)],
        format="JPEG",
        options={"quality": 95},
        default="default.jpg",
    )
    image2 = ProcessedImageField(
        upload_to="images/cafe",
        blank=False,
        processors=[ResizeToFill(1200, 760)],
        format="JPEG",
        options={"quality": 95},
        default="default.jpg",
    )
    image3 = ProcessedImageField(
        upload_to="images/cafe",
        blank=False,
        processors=[ResizeToFill(1200, 760)],
        format="JPEG",
        options={"quality": 95},
        default="default.jpg",
    )
    thumbnail1 = ImageSpecField(
        source="image1",
        processors=[ResizeToFill(120, 120)],
        format="JPEG",
    )
    thumbnail2 = ImageSpecField(
        source="image2",
        processors=[ResizeToFill(120, 120)],
        format="JPEG",
    )
    thumbnail3 = ImageSpecField(
        source="image3",
        processors=[ResizeToFill(120, 120)],
        format="JPEG",
    )
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    is_updated = models.BooleanField(default=False)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_articles"
    )
    bookmark_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="bookmark_articles"
    )
    hits = models.PositiveBigIntegerField(default=0, verbose_name="조회수")

    @property
    def created_time_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + "시간 전"
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + "일 전"
        else:
            return False


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cafe = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = FroalaField(
        options={
            "toolbarSticky": False,
            "heightMin": 300,
        }
    )
    rate = models.FloatField(
        default=3.0,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
    )
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    is_updated = models.BooleanField(default=False)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_reviews"
    )

    @property
    def like_count(self):
        return self.like_user_set.count()

    @property
    def created_time_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + "시간 전"
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + "일 전"
        else:
            return False


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=80)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    is_updated = models.BooleanField(default=False)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_comments"
    )
    parent = models.ForeignKey(
        "self",
        related_name="reply_set",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    @property
    def created_time_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + "시간 전"
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + "일 전"
        else:
            return False
