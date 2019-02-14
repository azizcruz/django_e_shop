from shop.models import Product
from django.conf import settings
from decimal import Decimal
from datetime import timedelta


class Cart(object):

    def __init__(self, request):
        ''' Initalize the cart '''

        self.session = request.session

        cart = self.session.get(settings.CART_SECRET_NAME)

        if not cart:
            cart = self.session[settings.CART_SECRET_NAME] = {}

        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)

        if product_id not in self.cart:

            self.cart[product_id] = {
            'product_name': product.name,
            'quantity': quantity,
            'price': str(product.price),
            'total_price': str(product.price * quantity)
            }
            self.session.modified = True
            self.session.set_expiry(int(timedelta(days=7, minutes=0, seconds=0).total_seconds()))

        else:

            self.cart[product_id]['quantity'] += quantity
            self.cart[product_id]['total_price'] = str(round(self.cart[product_id]['quantity'] * float(self.cart[product_id]['price']), 2))
            self.session.modified = True


    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

    def update_quantity(self, product, quantity=1):
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] = quantity
            self.cart[product_id]['total_price'] = str(round(float(self.cart[product_id]['quantity']) * float(self.cart[product_id]['price']), 2))
            self.session.modified = True

    def get_cart_content(self):
        product_ids = self.cart.keys()
        products = []

        for product_id in product_ids:
            product = {
            'product_id': product_id,
            'product_name': self.cart[product_id]['product_name'],
            'quantity': self.cart[product_id]['quantity'],
            'price': self.cart[product_id]['price'],
            'total_price': self.cart[product_id]['total_price']
            }

            products.append(product)

        return products

    def clear_all(self):
        if self.session[settings.CART_SECRET_NAME]:
            del self.session[settings.CART_SECRET_NAME]
            self.session.modified = True
