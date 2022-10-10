#!/usr/bin/env python3
"""
Redis Basics
"""
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable = None) -> Callable:
    """
    decorator that counts calls
    """
    name = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper method as described
        https://docs.python.org/3.7/library/functools.html#functools.wraps
        """
        self._redis.incr(name)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    Call History Decorator
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper function
        """
        input: str = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapper

def replay(func: Callable):
    """
    replay function
    """
    r = redis.Redis()
    func_name = func.__qualname__
    number_calls = r.get(func_name)
    try:
        number_calls = number_calls.decode('UTF-8')
    except Exception:
        number_calls = 0
    print(f'{func_name} was called {number_calls} times:')

    ins = r.lrange(func_name + ":inputs", 0, -1)
    outs = r.lrange(func_name + ":outputs", 0, -1)

    for cin, cout in zip(ins, outs):
        try:
            cin = cin.decode('UTF-8')
        except Exception:
            cin = ""
        try:
            cout = cout.decode('UTF-8')
        except Exception:
            cout = ""
        print(f'{func_name}(*{cin}) -> {cout}')


class Cache():
    """
    Redis Functionality
    """
    def __init__(self):
        """
        Constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()
    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores cache
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """
        reading from redis and recovering original type
        """
        key = self._redis.get(key)
        if fn:
            return fn(key)
        return key

    def get_str(self, key: str) -> str:
        """
        parameterized get string
        """
        return self._redis.get(key).decode('UTF-8')

    def get_int(self, key: str) -> int:
        """
        parameterized get int
        """
        value = self.redis.get(key)
        try:
            value = int(value.decode('UTF-8'))
        except Exception:
            value = 0
        return value
