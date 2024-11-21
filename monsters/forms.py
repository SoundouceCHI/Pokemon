from django import forms
from monsters.models import Pokemon

class PokemonForm(forms.ModelForm): 
    class Meta: 
        model= Pokemon
        fields= "__all__"