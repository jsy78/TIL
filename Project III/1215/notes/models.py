from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta, timezone

# Create your models here.
class Received_Note(models.Model):
    sent_username = models.CharField(max_length=30)
    received_username = models.CharField(max_length=30)
    received_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    is_important = models.BooleanField(default=False)
    is_trash = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)
    received_at = models.DateTimeField(null=True, blank=True)
    

    @property
    def sent_at_string(self):
        time = datetime.now(tz=timezone.utc) - self.sent_at

        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + "시간 전"
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.sent_at.date()
            return str(time.days) + "일 전"
        else:
            return self.sent_at.astimezone(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M")

    @property
    def received_at_string(self):
        if self.received_at == None:
            return "읽지 않음"

        time = datetime.now(tz=timezone.utc) - self.received_at

        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + "시간 전"
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.sent_at.date()
            return str(time.days) + "일 전"
        else:
            return self.received_at.astimezone(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M")


class Sent_Note(models.Model):
    sent_username = models.CharField(max_length=30)
    received_username = models.CharField(max_length=30)
    sent_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    received_at = models.DateTimeField(null=True, blank=True)
    received_note = models.OneToOneField(Received_Note, on_delete=models.SET_NULL, null=True)

    @property
    def sent_at_string(self):
        time = datetime.now(tz=timezone.utc) - self.sent_at

        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + "시간 전"
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.sent_at.date()
            return str(time.days) + "일 전"
        else:
            return self.sent_at.astimezone(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M")

    @property
    def received_at_string(self):
        if self.received_at == None:
            return "읽지 않음"

        time = datetime.now(tz=timezone.utc) - self.received_at

        if time < timedelta(minutes=1):
            return "방금 전"
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + "분 전"
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + "시간 전"
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.sent_at.date()
            return str(time.days) + "일 전"
        else:
            return self.received_at.astimezone(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M")
