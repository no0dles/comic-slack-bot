import feedparser
import re
from models import Comic

URL = "https://xkcd.com/rss.xml"
IMAGE_URL_REGEX = "<img src=\"(.*?)\""


def get_feed():
    feed = feedparser.parse(URL)
    pattern = re.compile(IMAGE_URL_REGEX)

    for entry in feed['entries']:
        try:
            Comic.get(Comic.url == entry['id'])
        except Comic.DoesNotExist:
            imgs = pattern.findall(entry['summary'])

            yield Comic.create(
                url=entry['id'],
                title=entry['title'],
                image_url=imgs[0] if len(imgs) > 0 else None,
                type='x'
            )