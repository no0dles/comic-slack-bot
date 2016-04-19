import feedparser
import re
from models import Comic
from comics.comic import ComicManager

URL = "http://explosm-feed.antonymale.co.uk/comics_feed"
IMAGE_URL_REGEX = "<img src=\"//(.*?)\""


class ExplosmComic(ComicManager):
    def fetch(self):
        feed = feedparser.parse(URL)
        pattern = re.compile(IMAGE_URL_REGEX)

        for entry in feed['entries']:
            try:
                Comic.get(Comic.url == entry['link'])
            except Comic.DoesNotExist:
                imgs = pattern.findall(entry['summary'])

                Comic.create(
                    url=entry['link'],
                    title=entry['title'],
                    image_url="http://" + imgs[0] if len(imgs) > 0 else None,
                    type='e'
                )

    def post(self, comic):
        payload = {
          "text": comic.title + " Link (" + comic.url + ")",
          "attachments": [{
              "image_url": comic.image_url
          }]
        }

        self.send_payload(payload)
        self.mark_comic(comic)
