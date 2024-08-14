from .models import Persons, Countries
from django import forms


class PersonsForm(forms.ModelForm):
    class Meta:
        model = Persons
        exclude = ["created_at"]


class CountriesForm(forms.ModelForm):
    class Meta:
        model = Countries
        exclude = ["created_at"]
