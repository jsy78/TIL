from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Hobby, Accepted, HobbyComment

class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = [
            'title',
            'category',
            'tags',
            'meeting_day',
            'address_type',
            'address',
            'X',
            'Y',
            'entry_fee',
            'content',
            'recruit_type',
            'limit',
            'image',
        ]

class HobbyUpdateForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = [
            'title',
            'meeting_day',
            'address',
            'entry_fee',
            'content',
            'image',
        ]
        labels = {
            'title': '소셜링 제목',
            'meeting_day': '소셜링 일시',
            'address': '소셜링 장소',
            'entry_fee': '활동비',
            'content': '소셜링 상세',
            'image': '이미지',
        }

class AcceptedForm(forms.ModelForm):
    class Meta:
        model = Accepted
        fields = []

class CommentForm(forms.ModelForm):
    class Meta:
        model = HobbyComment
        fields = [
            'content',
        ]