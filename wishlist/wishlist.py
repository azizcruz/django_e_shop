from shop.models import Product
from django.conf import settings

class Wishlist(object):

    def __init__(self, request):
        ''' Initialize the wishlist '''

        self.session = request.session

        wishlist = self.session.get(settings.WISHLIST_SECRET_NAME)

        if not wishlist:
            wishlist = self.session[settings.WISHLIST_SECRET_NAME] = {}

        self.wishlist = wishlist

    
    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.wishlist:
            self.wishlist[product.id] = {
                'product_image': str(product.get_image_url()),
                'product_name': product.name,
                'product_price': str(product.price),
                'product_url': product.get_absolute_url()
            }
            self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.wishlist:
            del self.wishlist[product_id]
            self.session.modified = True

    def get_wishlist(self):
        product_ids = self.wishlist.keys()
        products = []

        for product_id in product_ids:
            product = {
            'product_id': product_id,
            'product_image': self.wishlist[product_id]['product_image'],
            'product_name': self.wishlist[product_id]['product_name'],
            'product_url': self.wishlist[product_id]['product_url']
            }

            products.append(product)

        return products

        return self.wishlist
    
    def get_wishlist_session_content(self):
        return self.wishlist

    def clear_all(self):
        if self.session[settings.WISHLIST_SECRET_NAME]:
            del self.session[settings.WISHLIST_SECRET_NAME]
            self.session.modified = True
            return True
        else:
            return False