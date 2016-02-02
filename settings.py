import os
from urllib.parse import urlparse

if 'HEROKU' in os.environ:
    DEBUG = False
    url = urlparse(os.environ['DATABASE_URL'])
    DATABASE = {
        'engine': 'peewee.PostgresqlDatabase',
        'name': url.path[1:],
        'user': url.username,
        'password': url.password,
        'host': url.hostname,
        'port': url.port,
    }
else:
    DEBUG = True
    DATABASE = {
        'engine': 'peewee.PostgresqlDatabase',
        'name': 'comicbot',
        'user': 'postgres',
        'password': 'postgres',
        'host': 'localhost',
        'port': 5432 ,
        'threadlocals': True
    }

HOOK_URL = os.environ['HOOK_URL']