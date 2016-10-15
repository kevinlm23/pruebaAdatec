from django.conf.urls import patterns, url
from .views import (CreatePokemon, ListPokemon, home,DetailPokemon,UpdatePokemon,DeletePokemon,ListDeletePokemon, ListUpdatePokemon, wsListPokemon)

urlpatterns = [
    url(r'^create/$',CreatePokemon.as_view(), name = 'create'),
    url(r'^detail/(?P<pk>\d+)/$',DetailPokemon.as_view(), name = 'detail'),
    url(r'^detail/(?P<pk>\d+)/update/$',UpdatePokemon.as_view(), name = 'update'),
    url(r'^detail/(?P<pk>\d+)/delete/$',DeletePokemon.as_view(), name = 'delete'),
    url(r'^list/$',ListPokemon.as_view(), name = 'list'),
    url(r'^list_delete/$',ListDeletePokemon.as_view(), name = 'list_delete'),
    url(r'^list_update/$',ListUpdatePokemon.as_view(), name = 'list_update'),
    url(r'^$',home, name = 'home'),
    url(r'^ws_list_pokemon/$',wsListPokemon, name = 'ws_list_pokemon')
]