from django.contrib import admin
from .models import Band, Album  # Import models from the models.py file

# Register your models here.
admin.site.register(Band)
admin.site.register(Album)

