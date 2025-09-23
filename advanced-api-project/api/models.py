from django.db import models

class Author(models.Model):
    """
    Author model represents a writer who can have multiple books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a single book with its title, year, 
    and relationship to an Author (one-to-many).
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
