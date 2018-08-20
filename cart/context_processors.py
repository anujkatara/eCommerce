"""
A context processor is a python function that takes request object
 as an argument and returns a python dictionary which is added
to the request.Context processor are very important when you need
 to make something available to all Django templates
"""
from .cart import Cart


def cart(request):
    """ return a python dictionary which will be
     available to all templates render using request context """
    return {'cart': Cart(request)}
