from django.urls import path # type: ignore
from . import views
app_name='App_Login'
urlpatterns = [
    path( 'signup/' , views.sign_up , name="signup"),
    path( 'signin/' , views.login_page , name="login"), 
    path( 'logout/' , views.logot_user , name="logout"),
    path( 'profile/' , views.profile , name="profile"),
    path( 'change-profile/' , views.user_change  , name="user_change"),
    path( 'password/' , views.pass_change  , name="pass_change"),
    path( 'change-profile-image/' , views.add_profile_pic  , name="add_profile_pic"),
    path( 'change-image/' , views.change_profile_pic  , name="change_profile_pic"),
]