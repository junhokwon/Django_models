from django.contrib import admin

from django_models.models import Person
from .models import Person

admin.site.register(Person)
