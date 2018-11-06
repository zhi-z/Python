from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from booktest import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^login$',views.login),
    url(r'^login_check$',views.login_check),
    url(r'^change_pwd$',views.change_pwd),
    url(r'^change_pwd_action$',views.change_pwd_action),
]
