from django import forms
from .models import *

class CreatePokemonForm(forms.ModelForm):
    model = Pokemon
    fields = ["name",
              "type",
              "hability",
              "weight",
              "height",
              "description"]

