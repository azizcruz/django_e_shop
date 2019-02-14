from django.urls import re_path
from . import views

app_name = 'wishlist'

urlpatterns = [
    re_path(r'^$', views.wishlist, name='list_wishlist_products'),
    re_path(r'^wishlist/add$', views.add_to_wishlist, name='add_to_wishlist'),
    re_path(r'^(?P<id>\d+)/wishlist/remove$', views.remove_from_wishlist, name='remove_from_wishlist'),
    re_path(r'^clear/$', views.clear_all, name='clear_all')
]