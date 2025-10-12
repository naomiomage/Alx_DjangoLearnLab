Django Social Media API

This is a Django-based social media API project developed as part of the ALX Backend Specialization.
It allows users to perform CRUD operations for social media posts and is deployed on Render.

Project Overview

This project demonstrates a fully functional Django REST API with CRUD features, authentication, and deployment configuration.
It follows Django best practices for security, scalability, and maintainability.

Features

User registration and authentication

Create, read, update, and delete posts

Admin dashboard for managing content

RESTful API design

Deployed on Render with production settings

Tech Stack

Backend: Django, Django REST Framework

Database: PostgreSQL

Server: Gunicorn

Hosting: Render

Setup Instructions
1. Clone the Repository
git clone https://github.com/naomiomage/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Apply Migrations
python manage.py migrate

5. Run the Server Locally
python manage.py runserver


The app will be available at http://127.0.0.1:8000/

Production Configuration

In settings_prod.py:

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'alx-djangolearnlab-ho2p.onrender.com',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

Deployment

The app is live on Render at:
https://alx-djangolearnlab-ho2p.onrender.com

Author

Naomi Omage
ALX Backend Engineering Program