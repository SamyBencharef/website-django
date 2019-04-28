
from django.forms.widgets import *
from .models import Email, Commentary
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _


class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ['name', 'email', 'topic', 'message']
        labels = {
            'name': TextInput(attrs={'class': 'form-control'}) and _('Full name'),
            'email': EmailInput(attrs={'class': 'form-control'}) and _('Email'),
            'topic': TextInput(attrs={'class': 'form-control'}) and _('Subject'),
            'message': TextInput(attrs={'class': 'form-control'}) and _('Message'),
        }


class CommentaryForm(ModelForm):
    class Meta:
        model = Commentary
        fields = ['name_commentary', 'topic_commentary', 'message_commentary']
        labels = {
            'name_commentary': TextInput(attrs={'class': 'form-control'}) and _('Full name'),
            'topic_commentary': TextInput(attrs={'class': 'form-control'}) and _('Title'),
            'message_commentary': TextInput(attrs={'class': 'form-control'}) and _('Commentary'),
        }
