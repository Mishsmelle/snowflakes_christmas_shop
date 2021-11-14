from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    '''Contact form configurations'''
    class Meta:
        model = Contact

        fields = "__all__"