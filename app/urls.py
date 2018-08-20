"""url for shop app"""
from django.conf.urls import url
from . import views

app_name = 'app'

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail, name='product_detail'),
    url('login', views.user_login, name='login'),
    url('logout', views.user_logout, name='logout'),
    url(r'register', views.register, name='register'),

]
