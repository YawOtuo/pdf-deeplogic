from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'pdf/index.html'
    

