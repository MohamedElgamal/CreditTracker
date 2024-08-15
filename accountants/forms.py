from .models import Persons, Countries
from django import forms


class PersonsForm(forms.ModelForm):
    class Meta:
        model = Persons
        exclude = ["created_at"]

    def __init__(self, *args, **kwargs):
        super(PersonsForm, self).__init__(*args, **kwargs)
        self.fields["notes"].required = False
        self.fields["suspend_reason"].required = False


class CountriesForm(forms.ModelForm):
    class Meta:
        model = Countries
        exclude = ["created_at"]
