from comics import xkcd
from comics import explosm

feeds = [xkcd.get_feed, explosm.get_feed]

if __name__ == "__main__":
    for feed in feeds:
        feed()
