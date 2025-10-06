README (Documentation)

Overview



This project sets up a Social Media API with:



Django + Django REST Framework



Custom user model (with bio, profile picture, followers)



Token authentication (register, login, profile)



Setup Commands

pip install django djangorestframework

django-admin startproject social\_media\_api

cd social\_media\_api

python manage.py startapp accounts

python manage.py makemigrations

python manage.py migrate

python manage.py runserver





Access the API via:



http://127.0.0.1:8000/api/accounts/





\### Posts \& Comments API



\*\*Endpoints\*\*

\- `GET /api/posts/` — list posts (supports ?search=term and pagination)

\- `POST /api/posts/` — create post (Authorization: Token required)

\- `GET /api/posts/{id}/` — retrieve single post and its comments

\- `PATCH /api/posts/{id}/` — update post (owner only)

\- `DELETE /api/posts/{id}/` — delete post (owner only)



\- `GET /api/comments/?post={id}` — list comments for a post

\- `POST /api/comments/` — create comment (send {"post": id, "content": "..."}; Authorization required)

\- `PATCH/DELETE /api/comments/{id}/` — modify/delete comment (author only)



\*\*Pagination\*\*

\- Default page size is 10. Use `?page=` and `?page\_size=` (max 100).



\*\*Filtering / Search\*\*

\- Search posts by `title` or `content` using `?search=term`.



