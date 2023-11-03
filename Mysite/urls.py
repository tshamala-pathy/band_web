from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Mysite'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('band_detail/<int:pk>/', views.BandDetailView.as_view(), name='band_detail'),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]
