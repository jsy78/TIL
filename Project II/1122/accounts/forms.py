from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
    UsernameField,
)
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
            "address",
            "sido",
            "sigungu",
            "roadname",
            "email",
            "profile",
            "first_name",
            "last_name",
        )
        labels = {
            "username": "닉네임",
            "address": "주소",
            "sido": "시/도",
            "sigungu": "시/군/구",
            "roadname": "도로명",
            "email": "이메일",
            "profile": "프로필 이미지",
            "first_name": "이름",
            "last_name": "성",
        }
        widgets = {
            "address": forms.TextInput(
                attrs={
                    "readonly": "True",
                }
            ),
            "sido": forms.HiddenInput(
                attrs={
                    "readonly": "True",
                }
            ),
            "sigungu": forms.HiddenInput(
                attrs={
                    "readonly": "True",
                }
            ),
            "roadname": forms.HiddenInput(
                attrs={
                    "readonly": "True",
                }
            ),
        }

    def clean_username(self):
        username = self.cleaned_data["username"]
        if len(get_user_model().objects.filter(username=username)):
            raise ValidationError("중복된 아이디가 있습니다.")
        return username

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
            "last_name",
            "first_name",
            "profile",
            "address",
            "sido",
            "sigungu",
            "roadname",
            "email",
        )
        labels = {
            "last_name": "성",
            "first_name": "이름",
            "profile": "프로필 이미지",
            "address": "주소",
            "sido": "시/도",
            "sigungu": "시/군/구",
            "roadname": "도로명",
            "email": "이메일",
        }
        widgets = {
            "address": forms.TextInput(
                attrs={
                    "readonly": "True",
                }
            ),
            "sido": forms.HiddenInput(
                attrs={
                    "readonly": "True",
                }
            ),
            "sigungu": forms.HiddenInput(
                attrs={
                    "readonly": "True",
                }
            ),
            "roadname": forms.HiddenInput(
                attrs={
                    "readonly": "True",
                }
            ),
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if len(get_user_model().objects.filter(email=email)) >= 2:
            raise ValidationError("중복된 이메일이 있습니다.")
        return


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label="닉네임", widget=forms.TextInput(attrs={"autofocus": True})
    )
