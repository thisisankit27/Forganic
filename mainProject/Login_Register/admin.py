from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.CustomerProfile)
admin.site.register(models.Location)