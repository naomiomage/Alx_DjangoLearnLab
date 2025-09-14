# bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_protect
from .models import Book
from .forms import BookForm
from .forms import ExampleForm


# ---------------------------
# Show list of all books
# ---------------------------
@login_required
def book_list(request):
    books = Book.objects.all()  # ORM protects against SQL injection
    return render(request, "bookshelf/book_list.html", {"books": books})


# ---------------------------
# Example view to trigger a custom exception
# ---------------------------
def raise_exception(request):
    raise Http404("This is a forced exception for testing.")


# ---------------------------
# Alternative book list view
# ---------------------------
@login_required
def books(request):
    books = Book.objects.all()
    return render(request, "bookshelf/books.html", {"books": books})


# ---------------------------
# Add a book (requires permission)
# ---------------------------
@csrf_protect
@permission_required("bookshelf.can_create", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/form_example.html", {"form": form})


# ---------------------------
# Edit a book (requires permission)
# ---------------------------
@csrf_protect
@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/form_example.html", {"form": form})


# ---------------------------
# Delete a book (requires permission)
# ---------------------------
@csrf_protect
@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "bookshelf/form_example.html", {"form": None, "book": book})
