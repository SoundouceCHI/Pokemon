from django.shortcuts import render
from django.http import HttpRequest
from monsters.models import Pokemon

def view_index(request: HttpRequest): 
    pokemons = Pokemon.objects.all()
    return render(request, "core/page/index.html", {"pokemons": pokemons})