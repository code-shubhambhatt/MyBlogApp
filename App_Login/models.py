from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

# Create your models here.

class UserProfile(models.Model) :
    user = models.OneToOneField(User , related_name='user_profile', on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics')