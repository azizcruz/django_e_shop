from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartForm
from wishlist.forms import WishlistForm
from wishlist.wishlist import Wishlist
from django.conf import settings
from shop_auth.models import CustomUser
# Create your views here.

def list_products(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug == 'all':
        category = 'all'

    if category_slug and category_slug != 'all':
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }

    return render(request, 'shop/product/list.html', context)

def product_detail(request, id, slug=None):
    cart_form = CartForm()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    wishlist = Wishlist(request)

    if not slug:
        cart_form = CartForm(instance=product)

    # Check if the product is in wishlist otherwise set the wishlist form to None.
    if str(id) in wishlist.get_wishlist_session_content():
        wishlist_form = None
    else:
        wishlist_form = WishlistForm({'product_id': id})

    context = {
        'product': product,
        'cart_form': cart_form,
        'wishlist_form': wishlist_form
    }

    return render(request, 'shop/product/details.html', context)

def get_profile(request):
    user = get_object_or_404(CustomUser, username=request.user.username)
    context = {
        'active': user.active
    }
    return render(request, 'shop/user/profile.html', context)