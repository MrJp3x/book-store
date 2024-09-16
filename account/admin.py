
from .models import User, Profile

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    list_display = ('email', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", 'phone')


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
