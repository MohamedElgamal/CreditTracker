from django.shortcuts import render
from .models import Persons, Countries
from .forms import PersonsForm, CountriesForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

# Create your views here.


class CountryCreateView(CreateView):
    model = Countries
    form_class = CountriesForm
    template_name = "countries-create.html"
    success_url = reverse_lazy("create_countries")


class PersonsCreateView(CreateView):
    model = Persons
    form_class = PersonsForm
    template_name = "persons-create.html"
    success_url = reverse_lazy("create_persons")

    def form_valid(self, form):
        print("Before save")
        return super().form_valid(form)


class PersonsListView(ListView):
    model = Persons
    template_name = "persons-list.html"
    context_object_name = "persons"
