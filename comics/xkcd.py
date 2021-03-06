import feedparser
import re
from models import Comic
from comics.comic import ComicManager

URL = "https://xkcd.com/rss.xml"
IMAGE_URL_REGEX = "<img src=\"(.*?)\""


class XkcdComic(ComicManager):
    def fetch(self):
        feed = feedparser.parse(URL)
        pattern = re.compile(IMAGE_URL_REGEX)

        for entry in feed['entries']:
            try:
                Comic.get(Comic.url == entry['id'])
            except Comic.DoesNotExist:
                imgs = pattern.findall(entry['summary'])

                if len(imgs) == 0 or not imgs[0]:
                    continue

                Comic.create(
                    url=entry['id'],
                    title=entry['title'],
                    image_url=imgs[0],
                    type='x'
                )

    def post(self, comic):
        payload = {
          "text": comic.title + " Link (" + comic.url + ")"
        }

        self.send_payload(payload)
        self.mark_comic(comic)
