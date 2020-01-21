# djangoAsyncAdder
A django async app to add 2 numbers using redis and celery
# About
This is a Django Web App which uses Redis and Celery to add 2 numbers
# Installation
 - Install Redis by running `sudo apt install redis` This will install Redis and automatically start it
 - Clone this repo by running: `git clone https://github.com/vishalbala-nps/djangoAsyncAdder`
 - [Optional but recommended] Create a Virtual Environment by running `virtualenv -p python3 env` After creating the environment, activate it by running `source env/bin/activate`
 - After entering the environment, install the dependencies by running: `pip3 install -r requirements.txt`
 - After installing, start celery by running: `celery worker -A djangoAsync --loglevel=info`
 - Then, in another terminal, enter the virtual environment and navigete to the dir where the repo is cloned. Run the command: `python3 manage.py makemigrations` and `python3 manage.py migrate` to setup the SQLite3 db
 - Run the command: `python3 manage.py runserver` to start the server. You can access it at `127.0.0.1:8000`

