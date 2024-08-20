from .models import Persons, Countries
from django import forms


class PersonsForm(forms.ModelForm):
    class Meta:
        model = Persons
        exclude = ["created_at"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "identifier": forms.TextInput(attrs={"class": "form-control"}),
            "notes": forms.TextInput(attrs={"class": "form-control"}),
            "amount": forms.NumberInput(attrs={"class": "form-select"}),
            "nationality": forms.Select(attrs={"class": "form-select"}),
            "suspended": forms.NullBooleanSelect(attrs={"class": "form-control"}),
            "suspend_reason": forms.TextInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super(PersonsForm, self).__init__(*args, **kwargs)
        self.fields["notes"].required = False
        self.fields["suspend_reason"].required = False
        self.fields["nationality"].chioces = [
            (country.id, country.country) for country in Countries.objects.all()
        ]


class CountriesForm(forms.ModelForm):
    class Meta:
        model = Countries
        exclude = ["created_at"]
