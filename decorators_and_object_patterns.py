"""Decorators can wrap functions however they like, in this case we use a class.

Python's object orientation provides lots of goodies. Sometimes you might
want your decorator to meld with this.

In this example the decorated function returns an instance of a class
which provides the __enter__ and __exit__ methods required for use with
the Python `with` statement.


Concrete Example
----------------

contextlib.contextmanager

https://docs.python.org/3/library/contextlib.html?highlight=contextlib#contextlib.contextmanager

This decorator turns a generator into something that you can call using the
`with` statement e.g:

@contextlib.contextmanager
def myfunction():
    # do someting before the with block (in __enter__)
    yield
    # do something after the with block (in __exit__)

"""


def decorator(fcn):
    def _inner(*args, **kwargs):
        nonlocal fcn
        ctx = MyContext(fcn, *args, **kwargs)
        return ctx
    return _inner


class MyContext:
    def __init__(self, fcn, *args, **kwargs):
        self.fcn = fcn
        self.args = args
        self.kwargs = kwargs

    def __enter__(self):
        # do any required set up here (e.g. opening connections)
        print('enter')
        return self.fcn(*self.args, **self.kwargs)

    def __exit__(self, *_):
        # do any required tear down here (e.g. closing connections)
        print('exit')
        pass


@decorator
def function(*args):
    print('function', args)


print('1')
with function('a', 'b', 'c') as fcn:
    print('2')
print('3')
