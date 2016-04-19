import os
from urllib.parse import urlparse

if 'HEROKU' in os.environ:
    DEBUG = False
    DATABASE_URL = urlparse(os.environ['DATABASE_URL'])
    DATABASE = {
        'name': DATABASE_URL.path[1:],
        'user': DATABASE_URL.username,
        'password': DATABASE_URL.password,
        'host': DATABASE_URL.hostname,
        'port': DATABASE_URL.port,
    }
else:
    DEBUG = True
    DATABASE_URL = None
    DATABASE = {
        'name': 'comicbot',
        'user': 'postgres',
        'password': 'postgres',
        'host': 'localhost',
        'port': 5432 ,
        'threadlocals': True
    }

HOOK_URL = os.environ['HOOK_URL']