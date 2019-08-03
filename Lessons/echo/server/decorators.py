import logging
from functools import wraps

logger = logging.getLogger('decorators')


def logged(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        logger.debug(f'{func.__name__}: {request}')
        return func(request, *args, **kwargs)

    return wrapper


def logged_def(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.debug(f'{func.__name__}: {result}')
        return result

    return wrapper
