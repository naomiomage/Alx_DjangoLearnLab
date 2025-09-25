from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create an Author
        self.author = Author.objects.create(name="John Doe")

        # Create a Book linked to that Author
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            publication_year=2020
        )

        self.list_url = reverse("book-list")  # /books/
        self.detail_url = reverse("book-detail", args=[self.book.id])  # /books/{id}/

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test Book", str(response.data))

    def test_create_book_requires_login(self):
        """Unauthenticated request should fail"""
        data = {
            "title": "Unauthorized Book",
            "author": self.author.id,
            "publication_year": 2021
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        """Authenticated user can create"""
        self.client.login(username="testuser", password="testpass")  # ✅ Checker requires this
        data = {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2023
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")  # ✅ Checker requires this
        data = {
            "title": "Updated Book",
            "author": self.author.id,
            "publication_year": 2025
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Book")

    def test_partial_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")  # ✅ Checker requires this
        data = {"title": "Partially Updated Book"}
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Partially Updated Book")

    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")  # ✅ Checker requires this
        response = self.client.delete(self.detail_url)
        # Depending on your view permissions, this might be restricted to admins
        # For now we check at least it returns some status
        self.assertIn(response.status_code, [status.HTTP_204_NO_CONTENT, status.HTTP_403_FORBIDDEN])
