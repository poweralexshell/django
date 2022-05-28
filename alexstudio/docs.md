Installing django pip install django

django-admin startproject PROJECT_NAME - create new project run
py manage.py runserver - to start the app locally

Inside each project could be created different apps.
py manage.py startapp APP_NAME - new app instde the project

alexstudio/alexstudio/settings.py - to add new app to project next app name should be added to INSTALLED_APPS list

Inside app views.py needs to be modified. New function nedd to bee created

Create urls.py inside app dir with urlpatterns list