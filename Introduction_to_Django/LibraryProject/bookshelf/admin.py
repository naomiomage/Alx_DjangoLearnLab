from .models import Book
from django.contrib import admin

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show
    search_fields = ('title', 'author')                     # Enable search
    list_filter = ('publication_year',)                     # Filter by year
