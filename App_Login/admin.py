from django.contrib import admin #type:ignore
from .models import UserProfile #type:ignore
# Register your models here.

admin.site.register(UserProfile)