from django.conf import settings
from django.core.mail import mail_managers
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from contact.models import Message
from contact.forms import MessageForm


def send_message(request):
    """
    On a get request, show a form to allow visitors to send me a
    message.  On a post request, save the message in the database and
    send me an email.
    """
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = Message(sender_name=form.cleaned_data['sender_name'],
                sender_email=form.cleaned_data['sender_email'],
                body=form.cleaned_data['body'])
            if form.cleaned_data['ham_trap']:
                message.is_spam = True
            else:
                message_body = "%s (%s) said:\n\n%s\n" % (
                    form.cleaned_data['sender_name'],
                    form.cleaned_data['sender_email'],
                    form.cleaned_data['body'])
                mail_managers('photosbymonika.com contact message', message_body)
            message.save()
            return HttpResponseRedirect('%s?sent' % reverse(send_message))
    else:
        form = MessageForm()
    context = {
        'form': form,
        'sent': request.GET.has_key('sent'),
    }
    context.update(csrf(request))
    return render_to_response('contact/send_message.html', context,
        context_instance=RequestContext(request))