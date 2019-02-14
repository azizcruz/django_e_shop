from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from cart.forms import CartForm
from django.conf import settings

# Create your views here.

@require_POST
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart = Cart(request)
    cart_form = CartForm(request.POST)
    if cart_form.is_valid():
        data = cart_form.cleaned_data
        cart.add(product=product, quantity=data['quantity'])
        return redirect(product.get_absolute_url())



def remove_from_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart = Cart(request)
    cart.remove(product)

    return redirect('cart:cart_content')

def cart_content(request):
    cart_content = Cart(request)
    cart_content = cart_content.get_cart_content()
    total_price = 0

    if cart_content:
        for product in cart_content:
            total_price += float(product['total_price'])

    context = {
        'cart_content': cart_content,
        'total_price': round(total_price, 2)
    }

    return render(request, 'cart/content.html', context)

def edit_cart(request, id):
    instance = get_object_or_404(Product, id=id)
    cart_form = CartForm()
    context = {
        'instance': instance,
        'cart_form': cart_form
    }

    return render(request, 'cart/edit_cart.html', context)

def update_quantity(request, id):
    product = get_object_or_404(Product, id=id)
    cart = Cart(request)
    quantity = request.POST.get("quantity")

    cart.update_quantity(product, quantity=quantity)

    return redirect('cart:cart_content')


def clear_all(request):
    cart = Cart(request)
    cart.clear_all()
    return redirect('cart:cart_content')
