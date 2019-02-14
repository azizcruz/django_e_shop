from django.urls import re_path
from . import views

app_name = 'cart'

urlpatterns = [
    re_path(r'^$', views.cart_content, name='cart_content'),
    re_path(r'^(?P<id>\d+)/add$', views.add_to_cart, name='add_to_cart'),
    re_path(r'^(?P<id>\d+)/remove$', views.remove_from_cart, name='remove_from_cart'),
    re_path(r'^(?P<id>\d+)/edit$', views.edit_cart, name='edit_cart'),
    re_path(r'clearall/', views.clear_all, name='clear_all'),
    re_path(r'^(?P<id>\d+)/update_quantity$', views.update_quantity, name='update_quantity')
]
