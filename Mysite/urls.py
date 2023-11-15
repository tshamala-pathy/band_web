from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# Set the application namespace
app_name = 'Mysite'

# Define the URL patterns for the Mysite app
urlpatterns = [
    # Homepage view
    path('', views.IndexView.as_view(), name='index'),

    # Band detail view with a dynamic parameter for the band's primary key (pk)
    path('band_detail/<int:pk>/', views.BandDetailView.as_view(), name='band_detail'),

    # Login view using Django's built-in auth_views with a custom template
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Logout view using Django's built-in auth_views
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Signup view
    path('signup/', views.signup, name='signup'),
]
