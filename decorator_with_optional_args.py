"""Sometimes it is nice to make the arguments to decorators optional.

It's syntactic sugar but it helps make simple use cases a bit simpler.


Concrete Example
----------------

pytest.fixture

https://docs.pytest.org/en/latest/how-to/fixtures.html

This decorator takes arguments to handle more advanced use cases. If these
arguments are not required the brackets () can be omitted.

@pytest.fixture
def my_function_level_fixture():
    # this fixture lasts for the life of the test function
    yield
    # then after the function has been run any code after the `yield` will
    # be run

@pytest.fixture(scope='session')
def my_session_level_fixture():
    # this fixture lasts for the life of the entire test session
    yield
    # then after all of the tests have been run any code after the `yield` will
    # be run
"""

from functools import wraps


def print_call(fcn, args, kwargs):
    print(
        f'{fcn.__name__}('
        + ', '.join(str(arg) for arg in args)
        + ', '.join(f'{key}={value}' for key, value in kwargs.items())
        + ')'
    )


def decorator(fcn=None, **decorator_kwargs):
    if fcn:
        # no arguments provided to decorator
        @wraps(fcn)
        def _inner(*args, **kwargs):
            nonlocal fcn
            return fcn(*args, **kwargs)
        return _inner

    # arguments provided to decorator
    def _wrapper(fcn):
        @wraps(fcn)
        def _inner(*args, **kwargs):
            nonlocal fcn
            nonlocal decorator_kwargs
            print(f'decorator kwargs: {decorator_kwargs}')
            print_call(fcn, args, kwargs)
            return fcn(*args, **kwargs)
        return _inner
    return _wrapper


# decorator not provided any args and the () was omitted
@decorator
def function1(x, y, z):
    """function1 docstring."""
    print('inside function1', (x, y, z))


# decorator not provided any args
@decorator()
def function2(x, y, z):
    """function2 docstring."""
    print('inside function2', (x, y, z))


# decorator not provided kwargs
@decorator(answer=42)
def function3(x, y, z):
    """function3 docstring."""
    print('inside function3', (x, y, z))


function1(1, 2, 3)
function2(4, 5, 6)
function3(7, 8, 9)

print(function1.__doc__)  # note functools.wraps preserves the docstring
print(function2.__doc__)  # note functools.wraps preserves the docstring
print(function3.__doc__)  # note functools.wraps preserves the docstring
