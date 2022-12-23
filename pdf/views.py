from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic import TemplateView
from .models import Text
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import TextForm

# Create your views here.
class IndexView(FormView):
    template_name = 'pdf/index.html'
    form_class = TextForm
    context_object_name = "pdf_context"
    
    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        self.pdf_context = super().get_context_data(**kwargs)

        self.pdf_context['form'] = self.form_class
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs ):
        log_file = open('log.txt', 'w', encoding='utf-8')
        file = request.FILES['file']
        print(file.name, file = log_file)

        Text.objects.create(text=file.readlines(), filename=file.name)

        
        return render(request, self.template_name, {'form': self.form_class})

class TextListView(ListView):
    model = Text
    context_object_name = 'pdf_context'
    template_name='pdf/list.html'

    def get_queryset(self):
        return Text.objects.all()
            # Get 5 books containing the title war

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    
class TextDetailView(DetailView):
    model = Text
    template_name='pdf/detail.html'
    context_object_name = 'pdf_context'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context