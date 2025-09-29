from django.contrib import admin #type:ignore
from .models import Blog,Comment,Likes #type:ignore

# Register your models here.
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Likes)