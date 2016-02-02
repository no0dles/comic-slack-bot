from peewee import  Model, TextField, FixedCharField, BooleanField
from playhouse.db_url import connect
import os

db = connect(os.environ['DATABASE_URL'])


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
