from django.contrib import admin
from .models import User, Profile


class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "email")


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", 'phone')


admin.site.register(User, AccountAdmin)
admin.site.register(Profile, ProfileAdmin)
