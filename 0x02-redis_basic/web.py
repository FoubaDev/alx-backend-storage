#!/usr/bin/env python3
""" expiring web cache module """

from typing import Callable
from functools import wraps
import redis
import requests

redis = redis.Redis()


def wrap_requests(func: Callable) -> Callable:
    """ Decorator wrapper """

    @wraps(func)
    def wrapper(url):
        """ Wrapper for decorator guy """
        redis.incr(f"count:{url}")
        cached_response = redis.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode('utf-8')
        result = func(url)
        redis.setex(f"cached:{url}", 10, result)
        return result

    return wrapper


@wrap_requests
def get_page(url: str) -> str:
    """get page self descriptive
    """
    response = requests.get(url)
    return response.text
