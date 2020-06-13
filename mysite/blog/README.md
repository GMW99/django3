# Overview of files

## admin.py

This is where you registe models to included in the Django administration site - using this site is optional

## apps.py

This includes the main config of the blog (app) application

## migrations 

This directroy will contian database migrations of the applicaiton. Migrations allow Django to trakc your model changes and synchronize the database accordingly

## models.py

This includes the data models of your applications. All Django applications need to have a models.py file, but it can be left empty.

## tests.py

This is where tests for the application can be added.

## views.py

The logic of the application goes here, each view receives an HTTP request, processes it, and returns a response.