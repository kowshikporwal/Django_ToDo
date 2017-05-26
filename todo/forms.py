from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ContactForm(forms.Form):
    name = forms.CharField(required=False, max_length=100, help_text='100 characters max' )
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)
