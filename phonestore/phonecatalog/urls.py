from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
]
# the quotation marks is a string
