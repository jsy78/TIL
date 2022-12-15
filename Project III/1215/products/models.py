from django.db import models
from multiselectfield import MultiSelectField
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill, Thumbnail
from django.conf import settings
from datetime import datetime, timedelta
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    price = models.BigIntegerField()
    product_category = (
        ("사용감 있음", "사용감 있음"),
        ("거의 새 것", "거의 새 것"),
        ("미개봉", "미개봉"),
    )
    productType = models.CharField(max_length=20, choices=product_category, null=True)
    trade_category = (
        ("직거래", "직거래"),
        ("택배거래", "택배거래"),
    )
    tradeType = MultiSelectField(max_length=10, choices=trade_category, min_choices=1, max_choices=2)
    location = models.CharField(max_length=80, blank=True)
    image = ProcessedImageField(
        upload_to="images/product",
        blank=False,
        processors=[ResizeToFill(1200, 1200)],
        format="JPEG",
        options={"quality": 95},
        default="default.jpg",
    )
    thumbnail = ImageSpecField(
        source="image",
        processors=[Thumbnail(200, 200)],
        format="JPEG",
    )
    content = models.TextField()
    contentStripTag = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_updated = models.BooleanField(default=False)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_product")
    hits = models.PositiveBigIntegerField(default=0, verbose_name="조회수")

    @property
    def created_at_string(self):
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
            return self.created_at.astimezone(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M")

    @property
    def updated_at_string(self):
        time = datetime.now(tz=timezone.utc) - self.updated_at

        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + "시간 전"
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.updated_at.date()
            return str(time.days) + "일 전"
        else:
            return self.updated_at.astimezone(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M")


class Product_Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey(
        "self",
        related_name="reply_set",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_product_comment")

    @property
    def created_at_string(self):
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
            return self.created_at.astimezone(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M")

    @property
    def updated_at_string(self):
        time = datetime.now(tz=timezone.utc) - self.updated_at

        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + "시간 전"
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.updated_at.date()
            return str(time.days) + "일 전"
        else:
            return self.updated_at.astimezone(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M")
