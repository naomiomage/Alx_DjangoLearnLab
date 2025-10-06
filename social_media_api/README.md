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

