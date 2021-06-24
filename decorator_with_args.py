"""Decorators can take arguments.

These can be used for configuring the decorator's behaviour.


Concrete Example
----------------

functools.lru_cache

https://docs.python.org/3/library/functools.html?highlight=functools#functools.lru_cache

This is a decorator which memorises function calls in order to prevent
performing the same computation multiple times.

It takes a keyword argument called maxsize which sets the maximum number of
items permitted in the cache.

Note using keyword arguments is a good idea as it is easier to tell the
difference between the decorator being called with a function as the first
argument and the decorator being provided with kwargs.

"""

from functools import wraps


def print_call(fcn, args, kwargs):
    print(
        f'{fcn.__name__}('
        + ', '.join(str(arg) for arg in args)
        + ', '.join(f'{key}={value}' for key, value in kwargs.items())
        + ')'
    )


def decorator(*decorator_args):
    def _wrapper(fcn):
        @wraps(fcn)
        def _inner(*args, **kwargs):
            nonlocal fcn
            nonlocal decorator_args
            print(f'decorator args: {decorator_args}')
            print_call(fcn, args, kwargs)
            return fcn(*args, **kwargs)
        return _inner
    return _wrapper


@decorator('a', 'b', 'c')
def function(x, y, z):
    """function docstring."""
    print('inside function', x, y, z)


function(1, 2, 3)
print(function.__doc__)  # note functools.wraps preserves the docstring
