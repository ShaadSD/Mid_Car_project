from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from car.models import Car

# Create your views here.
from .forms import RegistrationForm

def register(request):
    if request.method=='POST':
        register_form=forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account created succesfully')
            return redirect('register')
    else:
        register_form=forms.RegistrationForm(request.POST)
    return render(request,'register.html',{'form':register_form,'type':'Register'})

def user_login(request):
    if request.method=='POST':
        form_login= AuthenticationForm(request,request.POST)
        if form_login.is_valid():
            user_name = form_login.cleaned_data['username']
            user_pass = form_login.cleaned_data['password']
            user=authenticate(username=user_name,password=user_pass)
            if user is not None:
                messages.success(request,'Login successfully')
                login(request,user)
                return redirect('profile')
            else:
                messages.warning(request, 'Login informtion incorrect')
                return redirect('register')
    else:
        form_login=AuthenticationForm()
    return render(request,'register.html',{'form':form_login,'type':'Login'})

def user_logout(request):
    logout(request)
    return redirect('user_login')

@login_required   
def Edit_profile(request):
    if request.method=='POST':
        edit_form=forms.Change_data(request.POST,instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request,'Profile updated succuessfull')
            redirect('profile')
    else:
        edit_form=forms.Change_data(instance=request.user)
    return render(request,'update_profile.html',{'form':edit_form})

def pass_change(request):
    if request.method == 'POST':
        form_pass = PasswordChangeForm(request.user, data=request.POST)
        if form_pass.is_valid():
            form_pass.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form_pass.user)
            return redirect('profile')
    
    else:
        form_pass=PasswordChangeForm(user=request.user)
    return render(request,'pass_change.html', {'form': form_pass})