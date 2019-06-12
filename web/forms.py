from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
  email = forms.EmailField(required=False)
  first_name = forms.CharField(max_length=30)
  last_name = forms.CharField(max_length=150)

  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['first_name'].widget.attrs.update({'style': 'color:black;'})
    self.fields['last_name'].widget.attrs.update({'style': 'color:black;'})
    self.fields['username'].widget.attrs.update({'style': 'color:black;'})
    self.fields['email'].widget.attrs.update({'style': 'color:black;'})
    self.fields['password1'].widget.attrs.update({'style': 'color:black;'})
    self.fields['password2'].widget.attrs.update({'style': 'color:black;'})

  def save(self, commit=True):
    user = super().save(commit=False)

    user.email = self.cleaned_data['username']
    user.username = self.cleaned_data['username']
    user.first_name = self.cleaned_data['first_name']
    user.last_name = self.cleaned_data['last_name']

    if commit:
      user.save()

    return user