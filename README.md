# OC Project 11: Improve Project P8 with new features "Forgotten Password Reset"

### Description

This project is part of the OC Python developer course.

The Pur Beurre start-up, for which you have already worked, decides to set up a web application that allows 
customers to find healthy alternatives (better nutriscore):

* The [OpenFoodFacts](https://fr.openfoodfacts.org/) Data
* Use of the Django web framework
* Test-driven development: unittest and functional test with Selenium
* Responsive interface with the Bootstrap CSS framework

### Functionalities 

* Search field from the home page
* The search must not be using AJAX
* The customer can create a user account and login/logout
* The customer can save searches and delete them
* The customer can see the details of the products
* Responsive interface

### New Feature
* Forgotten Password Reset:
  - Users can request a password reset
  - An email with password reset instructions is sent to the user

### Utilization and Software Needed
*On your local desktop
* Set up a virtual environment in your IDE (e.g., PyCharm or VSC)
* Use Python 3.11.4 
* Create your database (e.g., with pgAdmin 4)
* Configure the database in settings.py
* Make migrations
```
python manage.py makemigrations
python manage.py migrate
```

* Load the database with categories and products according to the categories listed in the constante.py file
which is in the directory /app_data_off/management/commands/constante.py
To do that, use the command in your terminal:
python manage.py cm_db
Run the local server in your IDE

# used to send email to users
* EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
* EMAIL_HOST = os.getenv('EMAIL_HOST')
* EMAIL_PORT = os.getenv('EMAIL_PORT', default=587)
* EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', default=True)
* EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
* EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
* EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'emails')  # new to test email in local

Emails are sent via Gmail, and two-factor authentication is required to obtain the application key "EMAIL_HOST_PASSWORD"

Note: The password reset developments were done locally and have not been deployed to Heroku like the P8 project.

# You can search alternatives for these categories (e.g.):

You can search alternatives for these categories (e.g.):

* Aides culinaires
* Chocolats
* Epicerie
* Poissons
* Rillettes de poissons
* Sardines à l'huile
* Viandes