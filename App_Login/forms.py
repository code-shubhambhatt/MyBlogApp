from django import forms #type:ignore
from django.contrib.auth.forms import UserCreationForm , UserChangeForm #type:ignore
from django.contrib.auth.models import User #type:ignore
from App_Login.models import UserProfile
class SignUpForm(UserCreationForm) :
    email = forms.EmailField(required=True)
    class Meta :
        model = User 
        fields = ('username' ,'email' , 'password1' ,'password2' )

class UserProfileChange(UserChangeForm):
    password = None   # 🚀 removes the password field completely

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']  # choose only fields you want

class ProfilePic(forms.ModelForm) :
    class Meta :
        model = UserProfile
        fields = ['profile_pic'] 