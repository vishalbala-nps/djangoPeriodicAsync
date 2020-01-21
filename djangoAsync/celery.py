import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoAsync.settings')

celery_app = Celery('djangoAsync')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
celery_app.conf.beat_schedule = {
    #name of the scheduler

    'add-every-1-min': {
        # task name which we have created in tasks.py

        'task': 'sum_of_2_nums',  
        # set the period of running
        
        'schedule': 60.0,
         # set the args 
         
    },
}