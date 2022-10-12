from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

# from .models import User

# Register your models here.
admin.site.register(
    get_user_model(),
    UserAdmin,
)
# admin.site.register(User, UserAdmin)
