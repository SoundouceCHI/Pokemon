from django.shortcuts import render, redirect
from django.http import HttpRequest
from uuid import UUID
from monsters.models import Pokemon
from django.http import Http404
from monsters.forms import PokemonForm
from django.contrib import messages

def view_pokemon(request: HttpRequest, uuid: UUID): 
    #pokemon detail page 
    try : 
        pokemon = Pokemon.objects.get(uuid=uuid)
    except: 
        raise Http404(f"Pokemon does not exist")
    
    return render(request,"monsters/page/pokemon-view.html", {'pokemon': pokemon})

def create_pokemon(request): 
    form = PokemonForm(request.POST or None) #soit avc donnes post si elle ne sont pas vide soit avc rien request.POST if true else None
    if request.POST and form.is_valid(): #rempli et valide 
        form.save()
        #ajouer msg de confirmation 
        messages.success(request, "Pokemon created sucessfully")
        #redirection 
        return redirect("index")
    return render(request, "monsters/page/pokemon-create.html", {"form": form})


def edit_pokemon(request: HttpRequest, uuid: UUID): 
    #pokemon detail page 
    try : 
        pokemon = Pokemon.objects.get(uuid=uuid)
    except: 
        raise Http404(f"Pokemon does not exist")
    
    form = PokemonForm(request.POST or None, instance=pokemon) #arg instance => l'objet de form est liee à l'objet pokemon du coup maj du form = maj du pokemon 
    if request.POST and form.is_valid(): 
        form.save()
        messages.success(request, "Pokemon edited sucessfully") 
        return redirect("index")
    return render(request, "monsters/page/pokemon-edit.html", {"form": form, "pokemon": pokemon})