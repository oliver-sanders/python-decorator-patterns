"""The majority of decorators fit this pattern.

This pattern is often used when you want to do something special before or
after the function is run.


Concrete Example
----------------

functools.partial

https://docs.python.org/3/library/functools.html?highlight=functools#functools.partial

This function "remembers" arguments for you, it is often used in places where
lambda functions might also be a solution.

>>> from functools import partial

>>> def function(x, y, z):
...     print(x, y, z)

we will "remember" the x and y arguments so we can use them later:
>>> fcn = partial(function, 1, 2)

the function returned takes only the z argument:
>>> fcn(3)
1 2 3
>>> fcn(4)
1 2 4

"""

from functools import wraps


def print_call(fcn, args, kwargs):
    print(
        f'{fcn.__name__}('
        + ', '.join(str(arg) for arg in args)
        + ', '.join(f'{key}={value}' for key, value in kwargs.items())
        + ')'
    )


# this is the decorator
def decorator(fcn):
    # this bit gets called when Python loads the module
    @wraps(fcn)
    def _inner(*args, **kwargs):
        # this bit gets called with the function is called
        nonlocal fcn
        # this line prints the call so we can see what it's doing
        print_call(fcn, args, kwargs)
        # this line calls the function using the provided args & kwargs
        return fcn(*args, **kwargs)
    # by returning _inner we are effectively replacing "fcn" with "_inner"
    return _inner


@decorator
def function():
    """function docstring"""
    print('inside function1')


function()
print(function.__doc__)  # note functools.wraps preserves the docstring
