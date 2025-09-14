# bookshelf/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.book_list, name="book_list"),
    path("raise-exception/", views.raise_exception, name="raise_exception"),
    path("all-books/", views.books, name="books"),
]
