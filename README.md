# url-shortner
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
 - cd url_shortner
 - python .\manage.py migrate

 > **Run application**
 - python .\manage.py runserver

*To change the database, change the database settings on the "/url_shortner/url_shortner/settings.py" path.*
