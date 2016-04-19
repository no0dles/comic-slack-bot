import os

if 'DATABASE_URL' in os.environ:
    DATABASE_URL = os.environ['DATABASE_URL']
    DATABASE = None
else:
    DATABASE_URL = None
    DATABASE = {
        'name': 'comicbot',
        'user': 'postgres',
        'password': 'postgres',
        'host': 'localhost',
        'port': 5432 ,
        'threadlocals': True
    }

if 'HEROKU' in os.environ:
    DEBUG = False
else:
    DEBUG = True

if 'HOOK_URL' in os.environ:
    HOOK_URL = os.environ['HOOK_URL']