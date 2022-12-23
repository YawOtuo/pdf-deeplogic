
from django import forms
from django.core.exceptions import RequestAborted, ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from django.utils.translation import gettext_lazy as _
from django.conf import settings    
from django.http import HttpResponse, HttpResponseRedirect, request
from django.core.mail import send_mail


from pdf.models import Text

# class DateInput(forms.DateInput):
#     input_type = 'date'

class TextForm(forms.Form):

    file = forms.FileField()  

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



   