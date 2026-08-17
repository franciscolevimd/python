import functools

from utils import is_authenticated
from utils import is_valid_password


def authenticate_class(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if is_authenticated(*args):
            return cls(*args, **kwargs)
        else:
            raise Exception("Usuario no autorizado.")
    return wrapper


def validate_password(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pwd = args[0].password
        if is_valid_password(pwd):
            return func(*args, **kwargs)
        else:
            raise Exception("Password apócrifo.")
    return wrapper
