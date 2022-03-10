from django.shortcuts import render
from user.forms import UserForm,UserProfileForm

from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import  HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,authenticate,logout




# Create your views here.
def index(request):
    return  render(request,'user/index.html')

def user_login(request):
    if request.method=="POST":
      username=request.POST.get("username")
      password = request.POST.get("password")
      user =authenticate(username=username,password=password)
      if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse('index'))
      else:
         return HttpResponse("User not found")
    else:
       return render(request,'user/login.html')

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def registration(request):
    registered=False
    if request.method=="POST":
        userForm=UserForm(request.POST)
        userProfileForm=UserProfileForm(request.POST)
        if(userForm.is_valid() and userProfileForm.is_valid()):
            user = userForm.save()   #return user object from userform
            user.set_password(user.password) # apply hash to the password
            userProfile=userProfileForm.save(commit=False)
            #dont save data in db, just return object because we need to set user and profile_pic
            userProfile.user=user
            if 'profile_pic' in request.FILES:
                userProfile.profile_pic=request.FILES['profile_pic']
                userProfile.save()
                registered=True
        else:
            print(userForm.errors,userProfileForm.errors )
    else:
        userForm=UserForm()
        userProfileForm=UserProfileForm()
    return render(request,'user/registration.html',{
        'registered':registered,
        'userForm':userForm,
        'userProfileForm':userProfileForm
    })

