from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api_app.views import Proper
from . import views


urlpatterns = [
    path('', views.SignupPage, name = 'signup'),
    path('login', views.LoginPage, name = 'login'),
    path('logout', views.LogoutPage, name = 'logout'),
    path('index', views.index, name = 'index'),
    path('view_all_prop', views.all_prop, name = 'all_prop'),
    path('add_prop', views.add_prop, name = 'add_prop'),
    path('remove_prop', views.remove_prop, name = 'remove_prop'),
    path('remove_prop/<int:prop_id>', views.remove_prop, name = 'remove_prop'),
    path('filter_prop', views.filter_prop, name = 'filter_prop'),
    path('api', Proper)   
]