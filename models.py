from peewee import Model, TextField, FixedCharField, BooleanField, PostgresqlDatabase
from settings import DATABASE, DATABASE_URL
from playhouse.db_url import connect

if DATABASE_URL:
    db = connect(DATABASE_URL)
else:
    db = PostgresqlDatabase(DATABASE['name'],
                            user=DATABASE['user'],
                            password=DATABASE['password'],
                            host=DATABASE['host'],
                            port=DATABASE['port'])


class BaseModel(Model):
    class Meta:
        database = db


class Comic(BaseModel):
    title = TextField()
    url = TextField()
    image_url = TextField()
    type = FixedCharField(max_length=1)
    posted = BooleanField(default=False)

db.create_table(Comic, True)
