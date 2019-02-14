from django.shortcuts import render, get_object_or_404, redirect
from .wishlist import Wishlist
from django.views.decorators.http import require_POST, require_GET
from shop.models import Product
# Create your views here.


def wishlist(request):
    wishlist = Wishlist(request)
    wish_content = wishlist.get_wishlist()

    context = {
        'wish_content': wish_content
    }

    
    return render(request, 'wishlist/list.html', context)


@require_POST
def add_to_wishlist(request):
    product_id = request.POST.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    wishlist = Wishlist(request)

    # Add to wishlist
    wishlist.add(product=product)

    print(request.session['wishlist'])

    return redirect(product.get_absolute_url())

def clear_all(request):
    wishlist = Wishlist(request)
    cleared = wishlist.clear_all()
    
    return redirect('wishlist:list_wishlist_products')


@require_GET
def remove_from_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    wishlist = Wishlist(request)
    wishlist.remove(product)

    return redirect('wishlist:list_wishlist_products')