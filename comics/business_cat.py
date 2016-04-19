import feedparser
from comics.comic import ComicManager
from models import Comic

URL = 'http://www.businesscat.happyjar.com/feed/'


class BussinessCatComic(ComicManager):
    def fetch(self):
        feed = feedparser.parse(URL)

        for entry in feed['entries']:
            try:
                Comic.get(Comic.url == entry['link'])
            except Comic.DoesNotExist:
                Comic.create(
                    url=entry['link'],
                    title=entry['title'],
                    image_url=entry['link'],
                    type='c'
                )

    def post(self, comic):
        payload = {
          "text": comic.title + " Link (" + comic.url + ")"
        }

        self.send_payload(payload)
        self.mark_comic(comic)
