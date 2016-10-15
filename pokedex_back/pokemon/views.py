from django.shortcuts import render
from django.core.urlresolvers import reverse
from models import *
from django.http import HttpResponse
from django.core import serializers
from forms import *
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

#Vista simples de inicio
def home(request):
    return render(request,'home.html')

class ListDeletePokemon(ListView):
    model = Pokemon
    template_name = "list_delete_pokemon.html"

class ListUpdatePokemon(ListView):
    model = Pokemon
    template_name = "list_update_pokemon.html"

#CBV de creacion pokemon
class CreatePokemon(CreateView):
    model = Pokemon
    fields = ["name",
              "type",
              "hability",
              "weight",
              "height",
              "description"]
    template_name = "pokemon_form.html"

    def get_success_url(self):
        return reverse("list")

#CBV de listado pokemon
class ListPokemon(ListView):
    model = Pokemon
    template_name = "list_pokemon.html"

#CBV de detaller pokemon
class DetailPokemon(DetailView):
    model = Pokemon
    template_name = "detail_pokemon.html"

#CBV de editar pokemon
class UpdatePokemon(UpdateView):
    model = Pokemon
    fields = ["name",
              "type",
              "hability",
              "weight",
              "height",
              "description"]
    template_name = "update_pokemon.html"

#CBV de eliminar pokemon
class DeletePokemon(DeleteView):
    model = Pokemon
    template_name = "delete_pokemon.html"

    def get_success_url(self):
        return reverse("list")

def wsListPokemon(request):
    data = serializers.serialize("json",Pokemon.objects.all())
    return HttpResponse(data,content_type='application/json')

