from django.contrib import admin
from accounts.models import CustomUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email')


admin.site.register(CustomUser, CustomUserAdmin)
