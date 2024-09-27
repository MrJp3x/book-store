from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile, PublisherProfile, AdminProfile
from .forms import UserCreationForm


class CustomUserAdmin(UserAdmin):
    """Admin view for managing the custom User model.

    Attributes:
        add_form (UserCreationForm): The form used for creating new users.
        form (UserChangeForm): The form used for changing existing users.
        list_display (tuple): The fields displayed in the user list view.
        list_filter (tuple): The fields used to filter users in the admin.
        search_fields (tuple): Fields used for searching users.
        ordering (tuple): Fields used for ordering the user list.
    """
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


class UserProfileAdmin(admin.ModelAdmin):
    """Admin view for managing UserProfile model."""
    list_display = ('user', 'first_name', 'last_name', 'birth_date', 'sex')
    search_fields = ('user__email', 'first_name', 'last_name')


class PublisherProfileAdmin(admin.ModelAdmin):
    """Admin view for managing PublisherProfile model."""
    list_display = ('user', 'company_name', 'publisher_manager', 'established_year')
    search_fields = ('user__email', 'company_name')


class AdminProfileAdmin(admin.ModelAdmin):
    """Admin view for managing AdminProfile model."""
    list_display = ('user', 'first_name', 'last_name', 'admin_type', 'birth_date')
    search_fields = ('user__email', 'first_name', 'last_name')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(AdminProfile, AdminProfileAdmin)
admin.site.register(PublisherProfile, PublisherProfileAdmin)
admin.site.register(User, CustomUserAdmin)
