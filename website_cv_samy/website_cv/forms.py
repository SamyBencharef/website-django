
from django.forms.widgets import *
from .models import Email
from django.forms import ModelForm


class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ['name', 'email', 'topic', 'message']
        labels = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'topic': TextInput(attrs={'class': 'form-control'}),
            'message': TextInput(attrs={'class': 'form-control'}),
        }

