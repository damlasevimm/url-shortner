# url-shortner
a simple URL shortener service using Django Rest Framework and SQLite

## TO SETUP
For running the application, please run the following commands on the commandline:

 1. python -m venv venv
 2. .\venv\Scripts\activate
 3. pip install -r requirements.txt
 4. cd url_shortner
 5. python .\manage.py migrate
 6. python .\manage.py runserver

To change the database, change the database settings on the "/url_shortner/url_shortner/settings.py" path.
