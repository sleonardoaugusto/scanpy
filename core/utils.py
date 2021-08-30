import typing
from time import sleep

from selenium.common.exceptions import NoSuchElementException


def retry(func: typing.Callable):
    def wrapper(self, times: int = 3, seconds: int = 2, *args, **kwargs):
        tries = 0
        while tries < times:
            try:
                func(self, *args, **kwargs)
                break
            except NoSuchElementException:
                sleep(seconds)
                continue

    return wrapper
