from django.urls import path
from .views import (
    BookListCreateView, BookDetailAPIView,   # DRF API Views
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView  # Django Generic Views
)

urlpatterns = [
    # --- API Endpoints ---
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail-api'),

    # --- Django Generic Views (HTML Pages) ---
   
