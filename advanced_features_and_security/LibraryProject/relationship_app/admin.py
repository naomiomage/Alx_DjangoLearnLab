from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "isbn")  # ✅ added isbn
    search_fields = ("title", "author", "isbn")  # optional for easy lookup
