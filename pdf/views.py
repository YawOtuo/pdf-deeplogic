from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic import TemplateView
from .models import Text
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import TextForm, NewUserForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login, authenticate , logout
from django.contrib import messages
from django.shortcuts import  render, redirect
from django.contrib.auth.forms import AuthenticationForm #add this
import io
from nanonets import NANONETSOCR
import environ
env = environ.Env()
environ.Env.read_env

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

        file = request.FILES['file']
        # print(file.read(), file=log_file)
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)[1:]
        # print(uploaded_file_url)
        model = NANONETSOCR()
        model.set_token("XQmXfZT6exouQq4zDoRSVsR3cuMVt6g1")
        file_path = r"C:\Users\User\OneDrive\Desktop\sterl\wellfound\deeplogic" + "/" + uploaded_file_url
        string = model.convert_to_string(file_path,formatting='lines and spaces') 

        # print(string)
        # print(file_path)

        new_text = Text.objects.create(text=string, filename=file.name, file_path=uploaded_file_url)
        new_text.save()
        # print(new_text.pk)

        # return render(request, self.template_name, {'form': self.form_class})
        return redirect('pdf:detail', pk=new_text.id)


class TextListView(ListView):
    model = Text
    context_object_name = 'pdf_context'
    template_name='pdf/list.html'

    def get_queryset(self):
        return Text.objects.all()

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
        

class RegisterView(TemplateView):
    
    template_name = 'pdf/registration/register.html'
    context_object_name = 'signup_context'
    form_class = NewUserForm()

    def get_context_data(self, **kwargs):
        self.signup_context = super().get_context_data(**kwargs)
        self.signup_context['register_form'] = self.form_class
        return self.signup_context

    def post(self, request, *args, **kwargs ):
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("pdf:index")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
        form = NewUserForm()
        return render (request=request, template_name="pdf/registration/register.html", context={"register_form":form})




class LoginView(TemplateView):
    template_name = 'pdf/registration/login.html'
    form_class = AuthenticationForm()
    context_object_name = "login_context"

    def get_context_data(self, **kwargs):
        self.login_context = super().get_context_data(**kwargs)
        self.login_context['login_form'] = self.form_class

        return self.login_context

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("pdf:index")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
        form = AuthenticationForm()
        return render(request=request, template_name="pdf/registration/login.html", context={"login_form":form})



class LogoutView(ListView):
    
    def get(self,request):

        logout(request)
        return redirect("pdf:login")
