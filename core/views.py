from django.shortcuts import render
from django.http import HttpRequest
from monsters.models import Pokemon
from monsters.forms import PokemonForm

def view_index(request: HttpRequest): 
    pokemons = Pokemon.objects.all()
    form = PokemonForm()
    return render(request, "core/page/index.html", {"pokemons": pokemons, "form": form})