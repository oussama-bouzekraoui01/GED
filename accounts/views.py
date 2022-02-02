from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm,UserCreationForm,PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from .models import *
from .forms import CreateUserForm, EditProfileForm

def home(request):
    return render(request, 'accounts/dashboard.html')

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('http://127.0.0.1:8000/index/')
        else:
            return redirect('http://127.0.0.1:8000/index/')
    return render(request, 'accounts/login.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request, 'accounts/register.html',context)

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)

def update(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
            
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/update.html', args)

def passwordChange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/passwordChange.html', args)

def profile(request):
    return render(request, 'accounts/profile.html')