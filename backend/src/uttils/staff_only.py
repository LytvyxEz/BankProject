from functools import wraps
from typing import Callable, Coroutine
import asyncio

from .try_except_deco import try_except

@try_except
def staff_only(user):
    def wrapper(func: Callable | Coroutine) -> Callable | Coroutine:
        if asyncio.iscoroutinefunction(func):    
        
            @wraps(func)
            async def async_wrapper(*args, **kwargs):
                ...
                return await func(*args, **kwargs)
            return async_wrapper
        
        else:
            @wraps(func)
            def sync_wrapper(*args, **kwargs):
                ...
                return func(*args, **kwargs)
            return sync_wrapper
        
    return wrapper
