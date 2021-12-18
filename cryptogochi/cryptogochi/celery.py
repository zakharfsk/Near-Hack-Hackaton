import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptogochi.settings')

app = Celery('cryptogochi')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update-datas-every-5-seconds':{
        'task': 'newsline.tasks.update_dates',
        'schedule': crontab()
    }
}