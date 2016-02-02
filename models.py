from peewee import Database, Model, TextField, FixedCharField, BooleanField
from settings import DATABASE

db = Database(DATABASE)


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
