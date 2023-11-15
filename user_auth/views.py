from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def user_login(request):
    """
    Render the login page.
    """
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    """
    Authenticate the user using the provided credentials.
    If authentication is successful, redirect to the index page.
    If authentication fails, redirect back to the login page.
    """
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
    # If authentication fails or the request method is not POST, return to the login page
    return HttpResponseRedirect(reverse('user_auth:login'))

@login_required
def show_user(request):
    """
    Display the user's information.
    """
    # Accessing the user's password is not recommended for security reasons
    return render(request, 'authentication/user.html', {
        "username": request.user.username
    })

def user_registration(request):
    """
    Handle user registration.
    If the form is valid, create a new user and log them in, then redirect to the authentication view.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_auth:authenticate_user')
    else:
        form = UserCreationForm()  # Use UserCreationForm for registration
    return render(request, 'authentication/registration.html', {'form': form})
