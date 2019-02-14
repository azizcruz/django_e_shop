from django.urls import re_path
from . import views

app_name = 'shop_auth'

urlpatterns = [
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate_user, name='activate'),
    re_path(r'^message/$', views.confirm_message, name='confirm_message'),
    re_path(r'^activated/$', views.activation_success, name='activation_success'),
    re_path(r'^request_activation/$', views.request_activation, name='request_activation')
]