from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create an Author object
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
        # ✅ Check response data
        self.assertIn("Test Book", str(response.data))

    def test_create_book(self):
        new_author = Author.objects.create(name="Jane Doe")
        data = {
            "title": "New Book",
            "author": new_author.id,
            "publication_year": 2023
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # ✅ Verify response contains the book title
        self.assertEqual(response.data["title"], "New Book")

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # ✅ Verify retrieved book title
        self.assertEqual(response.data["title"], "Test Book")

    def test_update_book(self):
        data = {
            "title": "Updated Book",
            "author": self.author.id,
            "publication_year": 2025
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # ✅ Verify update worked
        self.assertEqual(response.data["title"], "Updated Book")

    def test_partial_update_book(self):
        data = {"title": "Partially Updated Book"}
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # ✅ Verify partial update worked
        self.assertEqual(response.data["title"], "Partially Updated Book")

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
