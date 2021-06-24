"""Classes can be decorators too.

Because sometimes decorators get complex and you might want to take advantage
of some object orientated goodies.


Concrete Example
----------------

property

https://docs.python.org/3/library/functions.html?highlight=property#property

The property decorator returns a class with __get__ and __set__ methods
which allows it to behave as a descriptor:
https://docs.python.org/3/howto/descriptor.html#descriptor-howto-guide

>>> @property
... def x(): pass
>>> x.__get__  # doctest: +ELLIPSIS
<method-wrapper '__get__' of property object at ...>
>>> x.__set__  # doctest: +ELLIPSIS
<method-wrapper '__set__' of property object at ...>

"""


class Decorator:

    def __init__(self, fcn):
        self.fcn = fcn

    def __call__(self, *args, **kwargs):
        print('decorator')
        return self.fcn(*args, **kwargs)


@Decorator
def function():
    print('function')


function()
