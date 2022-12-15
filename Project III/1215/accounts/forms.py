from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import get_user_model
from .models import User

class DateInput(forms.DateInput):
    input_type = "Date"
   

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "password1",
            "password2",
            "birth",
            "image",
            "address",
            "address_detail",
            "gender",
            "sports",
            "travel",
            "art",
            "food",
            "develop",
            "nickname",
        ]
        widgets = {
            "birth": DateInput(),
        }
        
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = [
            "sports",
            "travel",
            "art",
            "food",
            "develop",
            "address",
            "address_detail",
            "image",
        ]
        widgets = {
            "birth": DateInput(),
        }

class CustomSocialForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = [
            "sports",
            "travel",
            "art",
            "food",
            "develop",
            "address",
            "address_detail",
            "image",
            "gender",
            "birth",
            "nickname",
        ]
        widgets = {
            "birth": DateInput(),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    def clean_new_password1(self):
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')

        if old_password == new_password1:
            raise forms.ValidationError('현재 암호와 동일합니다.')
        return new_password1
