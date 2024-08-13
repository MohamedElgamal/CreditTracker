from django.contrib import admin
from .models import FiscalYears, Countries, Transcations, Persons, Users

# Register your models here.
admin.site.register(FiscalYears)
admin.site.register(Countries)
admin.site.register(Transcations)
admin.site.register(Persons)
admin.site.register(Users)
