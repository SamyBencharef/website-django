
from django import forms
from django.forms.widgets import *
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):

    name = forms.CharField(label=_(u'Name'))
    email = forms.EmailField(label=_(u'Email'))
    topic = forms.CharField(label=_(u'Topic'))
    message = forms.CharField(widget=Textarea(), label=_(u'Message'))
    forward = forms.BooleanField(help_text="Check this box if you want a copy of your mail", required=False)
