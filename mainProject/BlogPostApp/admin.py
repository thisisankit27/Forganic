from django.contrib import admin
from . import models

# Permissions
class BlogAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

# Register your models here.

# admin.site.register(models.BlogPost)
admin.site.register(models.Blogs,BlogAdmin)
admin.site.register(models.Comment)