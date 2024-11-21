from django.db import models
from uuid import uuid4

class Pokemon(models.Model): 
    #attribut = instance de classe type 
    name = models.CharField(max_length=64, blank=False,unique=True, verbose_name="name") #je n'accepte ps de champs vide blank false 
    hp = models.PositiveSmallIntegerField(verbose_name="hit points")
    attack = models.PositiveSmallIntegerField(verbose_name="attack")
    defense = models.PositiveSmallIntegerField(verbose_name="defense")
    special_attack = models.PositiveSmallIntegerField(verbose_name="special attack")
    special_defense = models.PositiveSmallIntegerField(verbose_name="special defense")
    speed = models.PositiveSmallIntegerField(verbose_name="speed")
    legendary = models.BooleanField(default=False, verbose_name="legendary")
    description= models.TextField(blank=True, verbose_name="description", null=True)
    uuid = models.UUIDField(default=uuid4, editable=False, null=True)
    type1 = models.ForeignKey("monsters.Type1", on_delete=models.SET_NULL, null=True, verbose_name="element", related_name="pokemons") #application.model au lieu de faire un import 
    type2 = models.ForeignKey("monsters.Type2", on_delete=models.SET_NULL, null=True, verbose_name="effect")


    class Meta: 
        verbose_name="pokemon"
        verbose_name_plural= "pokemons"

    def __str__(self) -> str:
        return f"{self.name}"
