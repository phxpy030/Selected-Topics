from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Produce
from django.forms import ModelForm

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class Product(ModelForm):
    class Meta:
        model = Produce
        fields = ['ProductType','ProductImg','ProductName','ArtisName','Price','Material']


searchchoices = (
        ('Allbum', 'Allbum'),
        ('Card' , 'Card'),
        ('Photobook' , 'Photobook'),
        ('Poster' , 'Poster'),
    )

class SearchForm(forms.Form):
    SearchBy = forms.ChoiceField(choices=searchchoices)