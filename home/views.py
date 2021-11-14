"""Imports"""
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm


def home(request):
    """A view to render the contact page"""

    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message Sent!')

            instance = form.save()

            sender_email = instance.email
            subject = render_to_string(
                'home/contact_emails/subject_contact_email.txt',
                {'instance': instance})
            body = render_to_string(
                'home/contact_emails/body_contact_email.txt',
                {'instance': instance,
                 'contact_email': settings.DEFAULT_FROM_EMAIL})
            send_mail(
                subject,
                body, settings.DEFAULT_FROM_EMAIL,
                [sender_email]
            )
        else:
            messages.error(
                request,
                'Error, please check the form is valid')

    form = ContactForm()

    template = 'home/contact_us.html'
    context = {
        'form': form,
        'on_contact_page': True
    }

    return render(request, template, context)
