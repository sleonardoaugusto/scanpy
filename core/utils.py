from selenium.common.exceptions import NoSuchElementException

from logger import logger


def retry(func):
    def wrapper(retries: int = 3, *args, **kwargs):
        attempts = 0
        while attempts < retries:
            try:
                func(*args, **kwargs)
                break
            except NoSuchElementException as e:
                logger.info(e)
                continue

    return wrapper
