To run:

**Requirements
Python3.6

**Note: The project is created with Django to call the API at localhost. It is created with django-rest-framework which follows OpenAPI specifications and also uses standard HTTP verbs. Django REST Framework is superset of Swagger REST Framework.

1. Create a virtual environment
2. Install all the requirements given in requirements.txt
	pip install -r requirements.txt
3. in terminal run
	a. ./manage.py makemigrations
	b. ./manage.py migrate
	c. ./manage.py createsuperuser -> create your admin profile
	d. ./manage.py runserver 8080
4. RUN Mysql script [if no initial migration done] available in sqlquery.txt
5. Open browser and in new tab go to link: http://127.0.0.1:8080/admin and login with the admin account created.
6. To go through swagger doc -> http://127.0.0.1:8080/docs/
7. if you want to run other API's they can be accessed afer giving a /api/ in the url.
	a. http://127.0.0.1:8080/api/employees/
	b. http://127.0.0.1:8080/api/employees/<id>
	c. http://127.0.0.1:8080/api/employees/<id>/login [POST]
	d. http://127.0.0.1:8080/api/employees/<id>/logout
	c. http://127.0.0.1:8080/api/electronics/
	d. http://127.0.0.1:8080/api/electronics/<id>
	e. http://127.0.0.1:8080/api/electronics/<id>/stock/
