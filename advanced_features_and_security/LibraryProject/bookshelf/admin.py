from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book


# Register CustomUser properly
class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(CustomUser, CustomUserAdmin)


# Register Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author')
