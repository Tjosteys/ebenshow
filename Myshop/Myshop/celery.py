from __future__ import absolute_import
import os 
from celery import Celery
from django.conf import settings

#set th default Django settings module for the  'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Myshop.settings')

CELERY_BROKER = getattr(settings, 'CELERY_BROKER', 'redis://localhost:6379/5')

app = Celery('Myshop', broker=CELERY_BROKER) #, backend='redis', broker='redis://localhost:6379', include=['myshop.tasks'])


app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
	print('Request: {0!r}'.format(self.request))