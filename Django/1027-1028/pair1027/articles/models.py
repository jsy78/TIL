from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit
from imagekit.processors import Thumbnail
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    grade = models.IntegerField(
        validators=
        [MinValueValidator(1),
         MaxValueValidator(5)]
        )
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(1200, 960)],
                                format='JPEG',
                                options={'quality': 80})
    thumbnail = ProcessedImageField(blank=True,
                                    upload_to="thumbnail/",
                                    processors=[ResizeToFill(300, 200)],
                                    format="JPEG",
                                    options={"quality": 60},
                                    )
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='like_articles')
    
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)