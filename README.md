# Student-Management-System-using-Django

This repository contains a Python Django project for managing student registrations in an institution. The project includes a simple student registration system with the following features:

Pages
Student Registration Page: A form for adding new students. Each student can enroll in only one course, and each course can accommodate multiple students.
Student Details Page: Displays detailed information about each student.
Course Details Page: Shows details about each course.
Project Setup
To create and run this project, follow these steps:

Install Django: Ensure you have Python installed, then install Django using pip:

code:
"pip install django"
Create a Django Project: Start a new Django project with:

code:
"django-admin startproject myproject"
Create a Django App: Within your project directory, create an app for handling student registrations:

code:
"python manage.py startapp student_registration"
Set Up MVT Architecture:

Models: Define your database schema in models.py.

Views: Implement the business logic in views.py.

Templates: Create HTML templates in the templates directory for the UI.

Configure Database: Use SQLite as the default database. Make sure to configure it in settings.py and run migrations to create necessary tables:

code:
"python manage.py migrate"

Admin Interface: To view and manage data through Django’s admin interface, register your models in admin.py and create a superuser:

code:
"python manage.py createsuperuser"
Run the Project: Start the development server and view the application:

code:  
"python manage.py runserver"
Visit http://127.0.0.1:8000 in your browser to access the application and http://127.0.0.1:8000/admin to access the admin interface.
