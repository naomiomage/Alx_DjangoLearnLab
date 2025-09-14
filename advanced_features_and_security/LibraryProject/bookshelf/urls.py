# bookshelf/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.book_list, name="book_list"),
    path("raise-exception/", views.raise_exception, name="raise_exception"),
    path("all-books/", views.books, name="books"),

    # Secure CRUD routes
    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:pk>/edit/", views.edit_book, name="edit_book"),
    path("books/<int:pk>/delete/", views.delete_book, name="delete_book"),
]
