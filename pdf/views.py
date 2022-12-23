from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic import TemplateView
from .models import Text
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
        log_file = open('demo.txt', 'w')
        print(request.FILES['file'], file = log_file)
        return render(request, self.template_name, {'form': self.form_class})

