from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from apps.users.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserAdmin)