from django.contrib import admin
from .models import Tag, Category, Album

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Album)