# Import necessary modules and classes from Django
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import AuthenticationForm

# Import models and forms from the current Django app
from .models import Band
from .forms import CustomUserCreationForm

# Define a class-based view for the index page using ListView
class IndexView(ListView):
    """
    View for displaying a list of bands on the index page.

    Attributes:
        template_name (str): The name of the template to render.
        context_object_name (str): The variable name to use in the template for the list of bands.
        model (class): The model class representing the bands.

    """
    template_name = 'index.html'
    context_object_name = 'bands'
    model = Band

# Define a class-based view for displaying details of a specific band using DetailView
class BandDetailView(DetailView):
    """
    View for displaying details of a specific band.

    Attributes:
        template_name (str): The name of the template to render.
        model (class): The model class representing the band.
        context_object_name (str): The variable name to use in the template for the band object.

    """
    template_name = 'band_detail.html'
    model = Band
    context_object_name = 'band'

# Define a function-based view for user signup
def signup(request):
    """
    View for handling user registration/signup.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Mysite:login')  # Redirect to the 'login' view
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Define a function-based view for user login
def login_view(request):
    """
    View for handling user login.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """
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
