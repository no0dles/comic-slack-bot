from models import Comic
from playhouse.postgres_ext import fn
from comics.xkcd import XkcdComic
from comics.explosm import ExplosmComic
from comics.business_cat import BussinessCatComic


xkcd = XkcdComic()
explosm = ExplosmComic()
business_cat = BussinessCatComic()

comicManagers = [xkcd, explosm, business_cat]


def get_random_comic():
    return Comic.select().where(Comic.posted == False).order_by(fn.Random()).limit(1)


def post_comic():
    for random_comic in get_random_comic():
        if random_comic.type == 'x':
            xkcd.post(random_comic)
        elif random_comic.type == 'c':
            business_cat.post(random_comic)
        elif random_comic.type == 'e':
            explosm.post(random_comic)


if __name__ == "__main__":
    for comicManager in comicManagers:
        comicManager.fetch()

    post_comic()
