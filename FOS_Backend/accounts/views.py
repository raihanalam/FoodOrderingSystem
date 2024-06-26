from django.shortcuts import render, HttpResponseRedirect
from .forms import CreateNewUser, SigninForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse,reverse_lazy
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


def sign_up(request):
     my_form = CreateNewUser()
     registerd = False

     if request.method == 'POST':
          my_form = CreateNewUser(data=request.POST)
          if my_form.is_valid():
               user = my_form.save()
               registerd = True
               try:
                    user_profile = UserProfile(user=user)
                    user_profile.save()
                    messages.success(request,"Yor account has been created.")
                    return HttpResponseRedirect(reverse('Account_App:sign_in'))
               except:
                    messages.warning(request,"There is a problem creting in your accont. Please check and try again!")
               return HttpResponseRedirect(reverse('Account_App:sign_in'))

     return render(request,'signup.html',context={'title':'PhotoGram | Signup','form':my_form,'registerd':registerd})

def sign_in(request):
     form = SigninForm()
     if request.method == "POST":
          form = SigninForm(data=request.POST)
          if form.is_valid():
               username = form.cleaned_data.get('username')
               password = form.cleaned_data.get('password')
               user = authenticate(username=username,password=password)
               if user is not None:
                    login(request,user)
                    return HttpResponseRedirect(reverse('kitchen:home_page'))
               
     return render(request,'Account_App/signin.html',context={'title':'Signin Your Account','form':form})

@login_required
def sign_out(request):
     logout(request)
     return HttpResponseRedirect(reverse('Account_App:sign_in'))