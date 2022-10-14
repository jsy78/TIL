from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "content",
            "movie_name",
        ]
        labels = {
            "title": "리뷰 제목",
            "content": "리뷰 내용",
            "movie_name": "영화 이름",
        }
