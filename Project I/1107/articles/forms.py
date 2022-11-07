from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "image", "foodType"]
        labels = {
            "title": "가게 이름",
            "content": "후기",
            "image": "사진 첨부",
            "foodType": "음식 종류",
        }
        widgets = {
            "grade": forms.NumberInput(
                attrs={
                    "step": "0.5",
                    "max": "5.0",
                    "min": "0.5",
                }
            ),
        }
        exclude = ("user",)


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "댓글을 남겨보세요 💬",
            }
        ),
    )

    class Meta:
        model = Comment
        fields = [
            "content",
        ]


class ReplyForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "대댓글을 남겨보세요 💬",
            }
        ),
    )

    class Meta:
        model = Comment
        fields = [
            "content",
        ]
