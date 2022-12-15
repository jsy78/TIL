from django.contrib import admin
from .models import Categories, Hobby, Tag

# Register your models here.
admin.site.register(Categories)
admin.site.register(Tag)
admin.site.register(Hobby)
