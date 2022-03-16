from django.contrib import admin
from django.urls import path

from . import views


app_name = 'service'

urlpatterns = [
    path('', views.index, name='index'),
    path('search_staff/', views.search_staff, name='search_staff'),
    path('search_company/', views.search_company, name='search_company'),
    path('search_staff/exchange', views.exchange_search_staff,
         name='search_staff/exchange'),
    path('search_company/exchange', views.exchange_search_company,
         name='search_company/exchange')
]
