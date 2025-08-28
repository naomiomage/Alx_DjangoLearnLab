from django.contrib import admin

from .models import Book



@admin.register(Book)

class BookAdmin(admin.ModelAdmin):

&nbsp;   list\_display = ('title', 'author', 'publication\_year')  # Columns to show

&nbsp;   search\_fields = ('title', 'author')                     # Enable search

&nbsp;   list\_filter = ('publication\_year',)                     # Filter by year



