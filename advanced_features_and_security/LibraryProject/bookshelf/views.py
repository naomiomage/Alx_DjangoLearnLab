# bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden, Http404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book

# Show list of all books
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

# Example view to trigger a custom exception
def raise_exception(request):
    raise Http404("This is a forced exception for testing.")

# Alternative book view (similar to book_list)
@login_required
def books(request):
    books = Book.objects.all()
    return render(request, "bookshelf/books.html", {"books": books})
