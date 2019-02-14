from django.urls import re_path
from . import views

app_name = 'shop'

urlpatterns = [
    re_path(r'^profile/$', views.get_profile, name='get_profile'),
    re_path(r'^$', views.list_products, name='list_products'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.list_products, name='list_product_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
