import feedparser
import re
from models import Comic

URL = "http://explosm-feed.antonymale.co.uk/comics_feed"
IMAGE_URL_REGEX = "<img src=\"//(.*?)\""


def get_feed():
    feed = feedparser.parse(URL)
    pattern = re.compile(IMAGE_URL_REGEX)

    for entry in feed['entries']:
        try:
            Comic.get(Comic.url == entry['link'])
        except Comic.DoesNotExist:
            imgs = pattern.findall(entry['summary'])

            yield Comic.create(
                url=entry['link'],
                title=entry['title'],
                image_url="http://" + imgs[0] if len(imgs) > 0 else None,
                type='e'
            )
