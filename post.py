from models import Comic
from json import dumps
from playhouse.postgres_ext import fn
from settings import HOOK_URL
from requests import post
from comics import xkcd
from comics import explosm

feeds = [xkcd.get_feed, explosm.get_feed]


def get_random_comic():
    return Comic.select().where(Comic.posted == False).order_by(fn.Random()).limit(1)


def post_comic():
    for comic in get_random_comic():
        payload = {
          "title": comic.title,
          "title_link": comic.url,
          "attachments": [{
              "image_url": comic.image_url

          }]
        }

        post(HOOK_URL, data=dumps(payload))
        Comic.update(posted=True).where(Comic.id == comic.id).execute()

if __name__ == "__main__":
    for feed in feeds:
        for comic in feed():
            print(comic)

    post_comic()
