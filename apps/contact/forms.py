from django import forms


class MessageForm(forms.Form):

    """A form to handle messages submitted through the web site."""

    sender_name = forms.CharField(max_length=64, label='name')
    sender_email = forms.EmailField(label='email')
    body = forms.CharField(label='message', widget=forms.Textarea)
    ham_trap = forms.CharField(label='Leave this field blank', required=False)
