\# Advanced API Project



This Django REST Framework project demonstrates:

\- Custom serializers with nested relationships (Author \& Book).

\- Generic views for CRUD operations.

\- Custom validation (no future publication years, no duplicate book titles).

\- Permissions (read-only for guests, create/update for logged-in users, delete restricted to admins).



---



\## API Endpoints



\### Books

\- `GET /api/books/` → List all books (public).

\- `POST /api/books/` → Create a new book (authenticated users only).

\- `GET /api/books/<id>/` → Retrieve a book by ID (public).

\- `PUT /api/books/<id>/` → Update a book (authenticated users only).

\- `DELETE /api/books/<id>/` → Delete a book (admin only).



---



\## Permissions

\- \*\*Unauthenticated users:\*\* read-only access.

\- \*\*Authenticated users:\*\* can create and update books.

\- \*\*Admin users:\*\* can delete books.



---



\## Testing

Use Postman or curl:



```bash

\# List all books

GET http://127.0.0.1:8000/api/books/



\# Create a book (authenticated)

POST http://127.0.0.1:8000/api/books/

{

&nbsp; "title": "My New Book",

&nbsp; "publication\_year": 2025,

&nbsp; "author": 1

}



