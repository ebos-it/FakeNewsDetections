from newsPortal.newsPortal.newstraining.ntDriver import FNDDriver
from newsPortal.newsPortal.newsPortal.settings import log
import os


def main():
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", ".settings")
    log.debug("hello logger")
    fndDriver = FNDDriver()
    fndDriver.run()


if __name__ == "__main__":
    main()
