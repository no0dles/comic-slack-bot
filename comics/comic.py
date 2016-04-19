from requests import post
from settings import HOOK_URL
from models import Comic
from json import dumps


class ComicManager(object):
    def fetch(self):
        pass

    def post(self, comic):
        pass

    def send_payload(self, payload):
        post(HOOK_URL, data=dumps(payload))

    def mark_comic(self, comic):
        Comic.update(posted=True).where(Comic.id == comic.id).execute()
