from django import forms
from django.forms import ModelForm
from .models import Community, Comment


class CommunityForm(ModelForm):
    class Meta:
        model = Community
        fields = ("title", "content")
        labels = {
            "title": "제목",
            "content": "내용",
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        labels={
            'content':'댓글 내용',
        }


class ReCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        labels = {
            "content": "답글 내용",
        }
