from django.contrib import admin
from .models import User

class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "email")


admin.site.register(User, AccountAdmin)