from rest_framework import generics, permissions, serializers
from .models import Book
from .serializers import BookSerializer

# List all books and allow creating new books
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # anyone can read, only logged-in can create

    def perform_create(self, serializer):
        # This is our custom rule
        title = serializer.validated_data.get("title")
        if Book.objects.filter(title=title).exists():
            raise serializers.ValidationError({"title": "This book already exists."})
        serializer.save()

    # Allow anyone to read, only authenticated users can create
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Retrieve / Update / Delete a single book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == "DELETE":
            return [permissions.IsAdminUser()]  # ❌ Only admins can delete
        return [permissions.IsAuthenticatedOrReadOnly()] 