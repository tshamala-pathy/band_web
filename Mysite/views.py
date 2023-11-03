from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from .models import Band
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'bands'
    model = Band

class BandDetailView(DetailView):
    template_name = 'band_detail.html'
    model = Band
    context_object_name = 'band'

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Mysite:login')  # Redirect to the 'login' view
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('templates:index')  # Redirect to the 'index' view
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})