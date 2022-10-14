from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import CustomLetters
from django import forms


class CustomLettersForm(forms.ModelForm):
    class Meta:
        model = CustomLetters
        fields = ("to_email", "title", "content")
        labels = {
            "to_email": "받는 사람",
            "title": "제목",
            "content": "내용",
        }

    def clean_to_email(self):
        to_email = self.cleaned_data["to_email"]
        if not len(get_user_model().objects.filter(email=self.cleaned_data["to_email"])):
            raise ValidationError("이메일이 유효하지 않습니다.")
        return to_email
