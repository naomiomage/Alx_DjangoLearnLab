"""
BookList API:
- Requires authentication (Token).
- Only logged-in users can access.
- Token can be obtained at /api-token-auth/ by sending username & password.
"""


from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer