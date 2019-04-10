
from django.forms.widgets import *
from .models import Email, Commentary
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


class CommentaryForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ['nameEmail', 'dateEmail', 'topicEmail', 'messageEmail']
        labels = {
            'nameEmail': TextInput(attrs={'class': 'form-control'}),
            'dateEmail': DateInput(attrs={'class': 'form-control'}),
            'topicEmail': TextInput(attrs={'class': 'form-control'}),
            'messageEmail': TextInput(attrs={'class': 'form-control'}),
        }
