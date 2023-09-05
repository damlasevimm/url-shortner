# url-shortener
a simple URL shortener service using Django Rest Framework and SQLite

## TO SETUP
For running the application, please run the following commands on the commandline:

> **Create and activate the virtual environment**
 - python -m venv venv
 - source venv/bin/activate
 - .\venv\Scripts\activate (for Windows)

 > **Install the modules**
 - pip install -r requirements.txt

 > **Make database migrations**
 - cd url_shortener
 - python .\manage.py migrate url_shortener_api

 > **Run application**
 - python .\manage.py runserver

*To change the database, change the database settings on the "/url_shortener/url_shortener/settings.py" path.*

## TO RUN THE TEST CASES
For running the test cases, please run the following command on the commandline:
- python .\manage.py test