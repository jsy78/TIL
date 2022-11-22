from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
# https://docs.djangoproject.com/en/3.2/intro/tutorial07/
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "address",
        "role",
    )

admin.site.register(get_user_model(), AccountAdmin)