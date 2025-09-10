from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    register_view,
    login_view,
    logout_view,
    add_book,
    edit_book,
    delete_book,
)

urlpatterns = [
    # Book views
    path('books/', list_books, name='list_books'),
    path('books/add_book/', add_book, name='add_book'),          # add_book
    path('books/edit_book/<int:pk>/', edit_book, name='edit_book'),  # edit_book
    path('books/delete_book/<int:pk>/', delete_book, name='delete_book'),

    # Library detail view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication views
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
