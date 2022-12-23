from django.urls import path
from django.views.generic.edit import CreateView
from django.contrib import admin
from . import views

app_name = 'pdf'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('list', views.TextListView.as_view(), name='list'),
    path('detail/<pk>', views.TextDetailView.as_view() , name='detail'),


    
]

