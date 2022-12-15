from django import forms
from django.contrib.auth import get_user_model
from .models import Received_Note
from django.core.exceptions import ValidationError


class NoteForm(forms.ModelForm):
    class Meta:
        model = Received_Note
        fields = ("received_username", "title", "content")
        labels = {
            "received_username": "받는 사람",
            "title": "제목",
            "content": "내용",
        }
        widgets = {
            "received_username": forms.TextInput(
                attrs={
                    "placeholder": "받는 사람의 닉네임",
                }
            ),
        }

    def clean_received_username(self):
        received_username = self.cleaned_data["received_username"]
        if not get_user_model().objects.filter(nickname=received_username).exists():
            raise ValidationError("존재하지 않는 사용자입니다.")
        return received_username
