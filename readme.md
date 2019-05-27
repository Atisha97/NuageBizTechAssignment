To run:

<b>Requirements</b>
Python3.6

<b>Note</b>: <i>The project is created with Django to call the API at localhost. It is created with django-rest-framework which follows OpenAPI specifications and also uses standard HTTP verbs. Django REST Framework is superset of Swagger REST Framework.</i>

1. Create a virtual environment
2. Install all the requirements given in requirements.txt
	```
	pip install -r requirements.txt
	```
3. in terminal run
	* ./manage.py makemigrations
	* ./manage.py migrate
	* ./manage.py createsuperuser -> create your admin profile
	* ./manage.py runserver 8080
4. RUN Mysql script [if no initial migrations done] available in sqlquery.txt
5. Open browser and in new tab go to link: http://127.0.0.1:8080/admin and login with the admin account created.
6. To go through swagger doc -> http://127.0.0.1:8080/docs/
7. if you want to run other API's they can be accessed afer giving a /api/ in the url.
	* http://127.0.0.1:8080/api/employees/
	* http://127.0.0.1:8080/api/employees/1
	* http://127.0.0.1:8080/api/employees/1/login
	* http://127.0.0.1:8080/api/employees/1/logout
	* http://127.0.0.1:8080/api/electronics/
	* http://127.0.0.1:8080/api/electronics/1
	* http://127.0.0.1:8080/api/electronics/1/stock/

