from django.contrib import admin

# Register your models here.
from .models import Clicker
admin.site.register(Clicker) # Register clicker model onto the admin interface.