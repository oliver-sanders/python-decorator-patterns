"""You don't actually *have* to wrap a function with a decorator

Python lets you store arbitrary things on objects, decorators can simply
store data on the function for later use.

This attribute can be read by code that might call the function in order to
determine how to call it.


Concrete Example
----------------

cherrypy.expose

https://docs.cherrypy.org/en/3.3.0/tutorial/exposing.html

Cherrypy is a web server that allows you to expose Python functions as
HTTP(S) REST endpoints.

To tell which functions should and shouldn't be "exposed" to the network
they add an attribute to functions call "exposed".

For convenience and prettification they provide a decorator that does this
for us.

"""

from random import random


def decorator(fcn):
    fcn.x = random()
    return fcn


@decorator
def function1():
    pass


@decorator
def function2():
    pass


print(function1.x)
print(function2.x)
