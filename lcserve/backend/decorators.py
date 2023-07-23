import inspect
from functools import wraps
from typing import Callable, Dict


def serving(
    _func=None,
    *,
    websocket: bool = False,
    openai_tracing: bool = False,
    auth: Callable = None,
):
    def decorator(func):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            return await func(*args, **kwargs)

        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper = async_wrapper if inspect.iscoroutinefunction(func) else sync_wrapper
        _args = {
            'name': func.__name__,
            'doc': func.__doc__,
            'params': {
                'include_ws_callback_handlers': websocket,
                'openai_tracing': openai_tracing,
                # If websocket is True, pass the callback handlers to the client.
                'auth': auth,
            },
        }
        if websocket:
            wrapper.__ws_serving__ = _args
        else:
            wrapper.__serving__ = _args

        return wrapper

    return decorator if _func is None else decorator(_func)


def slackbot(
    _func=None,
    *,
    commands: Dict[str, Callable] = None,
    openai_tracing: bool = False,
):
    def decorator(func):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            return await func(*args, **kwargs)

        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper = async_wrapper if inspect.iscoroutinefunction(func) else sync_wrapper
        wrapper.__slackbot__ = {
            'name': func.__name__,
            'doc': func.__doc__,
            'params': {
                'commands': commands,
                'openai_tracing': openai_tracing,
            },
        }

        return wrapper

    return decorator if _func is None else decorator(_func)
