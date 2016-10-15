from django.test import TestCase
from models import *
from views import *
from django.http import HttpResponse
from django.core import serializers

# Create your tests here.
def wsListPokemon():
    data = serializers.serialize("json",Pokemon.objects.all())
    print data

def test_create_pokemon():
    try:
        create = Pokemon.objects.create(name = "Jolteon",
                                        type = "Electrico",
                                        hability = "Rayo",
                                        weight = 523,
                                        height = 125,
                                        description = "Amarillo")
        create.save()
        print "Se ha creado correctamente"
    except Exception as e:
        print "Error en la creacion del pokemon"


def test_list_pokemon():
    try:
        create = Pokemon.objects.all()
        for object in create:
            print ""
            print object.id
            print object.name
            print object.type
            print object.hability
            print object.weight
            print object.height
            print object.description
            print ""
    except Exception as e:
        print "Error al listar los pokemon"

def test_delete_pokemon():
    try:
        Pokemon.objects.filter(pk = 13).delete()
        print "Se ha eliminado correctamente"
    except Exception as e:
        print "No se pudo eliminar"

def test_update_pokemon():
    try:
        Pokemon.objects.filter(pk=12).update(hability="Trueno")
        print "Se ha actualizo correctamente"
    except Exception as e:
        print "No se pudo actualizar"