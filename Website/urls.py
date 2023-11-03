from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Mysite/', include('Mysite.urls')),
    path('', include('user_auth.urls')),
]
