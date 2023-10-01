from celery import Celery
import time

# broker config
app = Celery('tasks', backend='db+sqlite:///db.sqlite', broker='sqla+sqlite:///db.sqlite')

@app.task
def add(x, y):
    time.sleep(5)
    z = x + y
    return z

# run celery worker using this command : celery -A tasks worker --pool=solo -l info