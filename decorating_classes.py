"""Classes can be decorated as well as functions.

In this example the decorator adds an extra method to the class called "foo".

Inheritance would be better for this, but just as a quick demonstration of
what you can do with this approach.

Note the somewhat topic of metaclasses
https://realpython.com/python-metaclasses/


Concrete Example
----------------

dataclasses.dataclass

https://docs.python.org/3/library/dataclasses.html

The dataclass decorator bolts various methods onto a class based on the
arguments it was provided with.

@dataclass

>>> from dataclasses import dataclass

use the dataclass decorator on the class itself, it reads any properties
defined inside your class:
>>> @dataclass
... class MyClass:
...     x: str
...     y: int
...     z: bool

dataclass has bolted on some useful methods for us to use:
>>> MyClass.__eq__  # doctest: +ELLIPSIS
<function __create_fn__.<locals>.__eq__ at ...>
>>> MyClass.__lt__
<slot wrapper '__lt__' of 'object' objects>
>>> MyClass.__str__
<slot wrapper '__str__' of 'object' objects>

including the __init__ and __repr__ methods:
>>> MyClass('a', 1, True)
MyClass(x='a', y=1, z=True)

"""


def decorator(cls):
    def foo(self):
        print('foo')
    cls.foo = foo
    return cls


@decorator
class MyClass:
    pass


MyClass().foo()
# NOTE: flake8 raises an error on this line: "MyClass" has no attribute "foo"
# au contraire!
# this is a good example of the sort of issues you might start to run into
# by making things a little "too clever"
