""" Session for Cart """
from decimal import Decimal
from django.conf import settings
from app.models import Product


class Cart(object):
    """ cart class that will help us manage our shopping cart """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Method to add product into our cart
        """
        product_id = str(product.id)
        # product_id as the key in the cart content dictionary,
        # convert product id into a string because Django uses json to
        # serialize session data and json only allows string names.
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """
        Tracks changes in the cart and marks sessions as modified using
        self.session.modified = True
        """
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        """
        remove a single product from the cart and save the cart in the session
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
         Return the total number of items store in our cart.
         """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        total price of the items
        """
        return sum(
            Decimal(
                item['price']) * item['quantity']
            for item in self.cart.values()
        )

    def clear(self):
        """
        clear the session
        """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
