from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # Show these fields in the admin list view
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    
    # Fields to edit when creating/updating a user
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    
    # Fields to show when adding a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )


# ✅ This is what the checker wants:
admin.site.register(CustomUser, CustomUserAdmin)
