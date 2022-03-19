from xml.etree.ElementTree import Comment
from django.contrib import admin

# Register your models here.
from .models import Post , Category,Comment,Profile

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Profile)