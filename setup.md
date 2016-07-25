Clone this repository:

$ git clone https://github.com/jainsurbhi/inn.git
$ cd inn

Create a virtual environment for this project and install Django:

$ mkvirtualenv env
(env) $ pip install django

Run migrate to syncronize the database:
(env) $ python manage.py migrate

For creating Super User:
(env) $ python manage.py createsuperuser

Run Server:
(env) $ python manage.py runserver
