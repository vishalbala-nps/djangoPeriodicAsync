# djangoPeriodicAsync
A small demo/use of django periodic async task with Redis and Celery
## Overview
This is a small demo/use of Periodic async task in Django using Redis and Celery
## What does it do
A Periodic task is scheduled for every 1 minute. The task is to generate 2 random numbers and add it. The result is in JSON format and is dumped to a temporary file.

The view reads the temporary file and displays both the numbers, result and the published date
## Installation
-   Install Redis by running  `sudo apt install redis`  This will install Redis and automatically start it
-   Clone this repo by running:  `git clone https://github.com/vishalbala-nps/djangoPeriodicAsync`
-   [Optional but recommended] Create a Virtual Environment by running  `virtualenv -p python3 env`  After creating the environment, activate it by running  `source env/bin/activate`
-   After entering the environment, install the dependencies by running:  `pip3 install -r requirements.txt`
-   After installing, (at terminal 1) start celery by running:  `celery worker -A djangoAsync --loglevel=info`
-   In another terminal (at terminal 2) start celery beat by running: `celery -A djangoAsync beat -l info`
-   In another terminal(at terminal 3) Run the command:  `python3 manage.py runserver`  to start the server. You can access it at  `127.0.0.1:8000`
- You can look at terminal 1 and 2 where we can see our task get scheduled and run every minute
