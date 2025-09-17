from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet


# Create a router and register BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView from previous task)
    path('books/', BookList.as_view(), name='book-list'),

    # Routes from the router (CRUD operations)
    path('', include(router.urls)),
]