"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label='Name ')
    contact_email = forms.EmailField(required=True, label='Email ')
    message = forms.CharField(required=True, widget=forms.Textarea, label='Message')


class PageDetailsForm(forms.Form):
    name = forms.CharField(max_length=128, required=True, label='Unique Page Name')
    title = forms.CharField(max_length=128, required=True, label='Page title')
    url = forms.CharField(max_length=128, required=True, label='URL')
    published = forms.BooleanField(label='Published')
    metaDescription = forms.CharField(required=True, widget=forms.Textarea, label='Meta Description')

