from django.shortcuts import render # type: ignore
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm  # type: ignore 
from django.contrib.auth import login , authenticate , logout   # type: ignore 
from django.urls import reverse # type: ignore
from django.shortcuts import redirect # type: ignore
from django.contrib.auth.decorators import login_required   # type: ignore 
from App_Login.forms import SignUpForm , UserProfileChange , ProfilePic
from django.http import HttpResponseRedirect # type: ignore



# Create your views here.

def sign_up(request) :
    form = SignUpForm()
    registered = False
    if request.method == "POST" :
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {'form' : form ,
            'registered': registered}
    return render(request , 'App_Login/signup.html' ,context=dict)

def login_page(request) :
    form = AuthenticationForm()
    if request.method == "POST" :
        form = a=AuthenticationForm(data = request.POST)
        if form.is_valid() :
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username ,password=password )
            if user is not None : 
                login(request,user)
                return redirect('index')
    return render(request , 'App_Login/login.html' ,context={'form' : form})

@login_required
def logot_user(request) :
    logout(request)
    return redirect('App_Login:login')

@login_required
def profile(request) :
    return render(request,'App_Login/profile.html' , context= {})

@login_required
def user_change(request) :
    current_user = request.user
    form = UserProfileChange(instance= current_user)
    if request.method == "POST" :
        form = UserProfileChange(request.POST , instance = current_user )
        if form.is_valid() :
            form.save()
            form = UserProfileChange(instance= current_user )
    return render(request, 'App_Login/change_profile.html' , context={'form':form})

@login_required
def pass_change (request) :
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method =="POST" :
        form = PasswordChangeForm(current_user , data = request.POST) 
        if form.is_valid() :
            form.save()
            changed = True
    return render(request , 'App_Login/pass_change.html' , context= {'form':form ,'changed':changed})

@login_required
def add_profile_pic(request) :
    form = ProfilePic() 
    if request.method == "POST" :
        form = ProfilePic(request.POST ,request.FILES)
        if form.is_valid() :
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))

    return render(request , 'App_Login/profile_pic_add.html' , context={'form':form})

@login_required
def     change_profile_pic (request) :
    form = ProfilePic(instance = request.user.user_profile)
    if request.method =="POST" :
        form = ProfilePic(request.POST , request.FILES ,instance = request.user.user_profile)
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request ,'App_Login/profile_pic_add.html', context={'form':form})