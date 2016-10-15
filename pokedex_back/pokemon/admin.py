from django.contrib import admin
from models import *
# Register your models here.

class PokemonAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'type')
    fieldsets = (
        ("Information", {
            'fields': ('name', 'type','hability','weight','height', 'description')
        }),
    )

admin.site.register(Pokemon, PokemonAdmin)