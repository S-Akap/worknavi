from django.contrib import admin
from django.urls import path

from . import views


app_name = 'service'

urlpatterns = [
    path('', views.index, name='index'),
    path('search_stuff/', views.search_stuff, name='search_stuff'),
    path('search_company/', views.search_company, name='search_company'),
    path('search_stuff_func/', views.search_stuff_func, name='search_stuff_func'),
    path('api/', views.exchange_search_stuff_data,
         name='api'),
]
