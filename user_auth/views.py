from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm 


def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    if request.method == 'POST':
        # Use AuthenticationForm to validate the user's credentials
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Mysite:index')
        # If authentication fails, return to the login page
    return HttpResponseRedirect(reverse('user_auth:login'))

@login_required
def show_user(request):
    # Accessing the user's password is not recommended for security reasons
    return render(request, 'authentication/user.html', {
        "username": request.user.username
    })

def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_auth:authenticate_user')
    else:
        form = UserCreationForm()  # Use UserCreationForm for registration
    return render(request, 'authentication/registration.html', {'form': form})
