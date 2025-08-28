\# CRUD Operations for Book Model



\## Create

\*\*Command used:\*\*

```python

from bookshelf\_app.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication\_year=1949)

book

```



\*\*Output:\*\*

```python

<Book: 1984 by George Orwell (1949)>

```



\## Retrieve

\*\*Command used:\*\*

```python

Book.objects.all()

```



\*\*Output:\*\*

```python

<QuerySet \[<Book: 1984 by George Orwell (1949)>]>

```



\## Update

\*\*Command used:\*\*

```python

book = Book.objects.get(title="1984")

book.title = "Nineteen Eighty-Four"

book.save()

book

```



\*\*Output:\*\*

```python

<Book: Nineteen Eighty-Four by George Orwell (1949)>

```



\## Delete

\*\*Command used:\*\*

```python

book.delete()

Book.objects.all()

```



\*\*Output:\*\*

```python

<QuerySet \[]>

```



