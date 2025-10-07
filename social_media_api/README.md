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





#### **# Social Media API (Django + DRF)**



A simple social media API built with \*\*Django Rest Framework\*\*, allowing users to register, log in, follow others, create posts, and view a personalized feed.



---



\##  Features



\- User Registration \& Authentication (Token-based)

\- Follow / Unfollow System

\- Create and View Posts

\- Personalized Feed (shows posts from followed users)

\- Profile View (who you follow / your followers)



---



\##  Technologies Used



\- Python 3

\- Django 5+

\- Django Rest Framework (DRF)

\- SQLite (default)

\- cURL or Postman for testing API endpoints



---



\##  **Setup Instructions**



\### 1. Clone the Repository

```bash

git clone <your\_repo\_url>

cd social\_media\_api

````



\### 3. **Install Dependencies**



```bash

pip install -r requirements.txt

```



\### 4. Run Migrations



```bash

python manage.py migrate

```



\### 5. Run the Development Server



```bash

python manage.py runserver

```



---



\## **API Endpoints \& cURL Testing**



\### 1. Register a User



```bash

curl -X POST -H "Content-Type: application/json" -d "{\\"username\\":\\"joy\\", \\"password\\":\\"1234\\"}" http://127.0.0.1:8000/api/accounts/register/

```



\*\*Response:\*\*



```json

{"token":"<token>", "username":"joy"}

```



\### 2. Login a User



```bash

curl -X POST -H "Content-Type: application/json" -d "{\\"username\\":\\"joy\\", \\"password\\":\\"1234\\"}" http://127.0.0.1:8000/api/accounts/login/

```



\*\*Response:\*\*



```json

{"token":"<token>"}

```



\### 3. View Profile



```bash

curl -H "Authorization: Token <token>" http://127.0.0.1:8000/api/accounts/profile/

```



\### 4. Follow / Unfollow Users



\*\*Follow a user (replace `<user\_id>`):\*\*



```bash

curl -X POST -H "Authorization: Token <token>" http://127.0.0.1:8000/api/accounts/follow/<user\_id>/

```



\*\*Unfollow a user:\*\*



```bash

curl -X POST -H "Authorization: Token <token>" http://127.0.0.1:8000/api/accounts/unfollow/<user\_id>/

```



\### 5. View Followers \& Following



```bash

\# Who you follow

curl -H "Authorization: Token <token>" http://127.0.0.1:8000/api/accounts/me/following/



\# Your followers

curl -H "Authorization: Token <token>" http://127.0.0.1:8000/api/accounts/me/followers/

```



\### 6. Create a Post



```bash

curl -X POST -H "Authorization: Token <token>" -H "Content-Type: application/json" -d "{\\"title\\":\\"My first post\\", \\"content\\":\\"Testing feed system!\\"}" http://127.0.0.1:8000/api/posts/

```



\### 7. View Feed



```bash

curl -H "Authorization: Token <token>" "http://127.0.0.1:8000/api/feed/?page=1"

```



---



\## Example Test Flow



```bash

\# Register 2 users

curl -X POST -H "Content-Type: application/json" -d "{\\"username\\":\\"joy\\", \\"password\\":\\"1234\\"}" http://127.0.0.1:8000/api/accounts/register/

curl -X POST -H "Content-Type: application/json" -d "{\\"username\\":\\"joy2\\", \\"password\\":\\"1234\\"}" http://127.0.0.1:8000/api/accounts/register/



\# joy2 creates a post

curl -X POST -H "Authorization: Token <joy2\_token>" -H "Content-Type: application/json" -d "{\\"title\\":\\"My first post\\", \\"content\\":\\"Testing feed system!\\"}" http://127.0.0.1:8000/api/posts/



\# joy follows joy2

curl -X POST -H "Authorization: Token <joy\_token>" http://127.0.0.1:8000/api/accounts/follow/2/



\# joy’s feed shows joy2’s post

curl -H "Authorization: Token <joy\_token>" "http://127.0.0.1:8000/api/feed/?page=1"

```



---



\##  Project Structure



```

social\_media\_api/

│

├── accounts/

│   ├── serializers.py

│   ├── views.py

│   ├── urls.py

│   └── models.py

│

├── posts/

│   ├── serializers.py

│   ├── views.py

│   ├── urls.py

│   └── models.py

│

├── social\_media\_api/

│   ├── settings.py

│   ├── urls.py

│   └── wsgi.py

│

└── manage.py

```



---



\##  Author



\*\*Naomi Omage\*\*

ALX Django Learner |  Building REST APIs

&nbsp;Nigeria



---



\##  Notes



\* Make sure your server is running before using curl.

\* Replace `<token>` and `<user\_id>` with actual values returned from registration/login.

\* You can also view endpoints in your browser using \[DRF’s built-in API interface](http://127.0.0.1:8000/api/).





##### \### **Likes \& Notifications**



\- POST `/api/posts/<post\_id>/like/` — Like a post (Auth required)

\- POST `/api/posts/<post\_id>/unlike/` — Unlike a post (Auth required)

\- GET `/api/notifications/` — List your notifications (Auth required)

\- POST `/api/notifications/<id>/read/` — Mark a notification read (Auth required)



Notifications are generated when:

\- someone likes your post

\- someone comments on your post (if you add that hook)

\- someone follows you (if you add that hook)









