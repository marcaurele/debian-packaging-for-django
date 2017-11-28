# import multiprocessing
import os

from mysite import read_environ

# workers = multiprocessing.cpu_count() * 2 + 1
workers = 1
bind = '127.0.0.1:8000'
errorlog = '/var/log/django-polls.log'
timeout = graceful_timeout = 60


def on_reload(server):
    server.log.info("Reading environ")
    os.environ = read_environ()
    server.log.info(os.environ)
