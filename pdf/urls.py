from django.urls import path
from django.views.generic.edit import CreateView

from . import views

app_name = 'pdf'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    
]

