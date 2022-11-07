from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
    )

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "nickname",
            "profile",
            "first_name",
            "last_name",
            "email",
        )
        labels = {
            "username": "아이디",
            "nickname": "닉네임",
            "profile": "프로필 이미지",
            "first_name": "이름",
            "last_name": "성",
            "email": "이메일",
        }

    def clean_username(self):
        username = self.cleaned_data["username"]
        if len(get_user_model().objects.filter(username=username)):
            raise ValidationError("중복된 아이디가 있습니다.")
        return username

    def clean_nickname(self):
        nickname = self.cleaned_data["nickname"]
        if len(get_user_model().objects.filter(nickname=nickname)):
            raise ValidationError("중복된 닉네임이 있습니다.")
        return nickname

    def clean_email(self):
        email = self.cleaned_data["email"]
        if len(get_user_model().objects.filter(email=email)):
            raise ValidationError("중복된 이메일이 있습니다.")
        return email


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(
        required=True,
    )

    class Meta:
        model = get_user_model()
        fields = (
            "nickname",
            "profile",
            "first_name",
            "last_name",
            "email",
        )
        labels = {
            "nickname": "닉네임",
            "profile": "프로필 이미지",
            "first_name": "이름",
            "last_name": "성",
            "email": "이메일",
        }

    def clean_nickname(self):
        nickname = self.cleaned_data["nickname"]
        if len(get_user_model().objects.filter(nickname=nickname)) >= 2:
            raise ValidationError("중복된 닉네임이 있습니다.")
        return nickname

    def clean_email(self):
        email = self.cleaned_data["email"]
        if len(get_user_model().objects.filter(email=email)) >= 2:
            raise ValidationError("중복된 이메일이 있습니다.")
        return email
