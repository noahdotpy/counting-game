from django.contrib import admin

# Register your models here.
from .models import Counter
admin.site.register(Counter) # Register counter model onto the admin interface.