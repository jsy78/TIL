from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

# Register your models here.

admin.site.register(get_user_model(), UserAdmin)
UserAdmin.fieldsets += (("Custom fields", {"fields": ("nickname", "gender", "address", "address_detail", "birth", "kakao_id", "followings", "image", "sports", "art", "travel", "food", "develop")}),)