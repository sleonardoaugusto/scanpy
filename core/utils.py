from selenium.common.exceptions import NoSuchElementException

from logger import logger


def retry(retries: int = 1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    func(*args, **kwargs)
                    break
                except NoSuchElementException as e:
                    logger.info(e)
                    continue

        return wrapper

    return decorator
