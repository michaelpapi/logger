from django.contrib import admin

from .models import Logg, Loggs

# Register your models here.

admin.site.register(Logg)
admin.site.register(Loggs)