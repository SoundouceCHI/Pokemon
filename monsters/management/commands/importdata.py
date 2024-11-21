from typing import Any
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from pathlib import Path
import csv 
from monsters.models import Type1, Type2, Pokemon


PATH = Path(__file__).parent/"pokemon.csv" #get the path of the file pokemon, must be in tha same directory as the current file 
class Command(BaseCommand): 
    def add_arguments(self, parser: CommandParser) -> None:
        return super().add_arguments(parser)
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        with open(PATH, "r", encoding="utf-8") as file: 
            reader= csv.DictReader(file)
            values = set()
            for row in reader: 
                values.add(row["Type 1"])

        #save values in db 
        Type1.objects.all().delete()
        for value in values : 
            Type1.objects.create(name=value, description="")
        
        for item in Type1.objects.all(): 
            print(f"Type1: {item.name}")


        # Step 2: Import Type 2
        # Read distinct Type 2 values from the CSV file
        with open(PATH, "r", encoding="utf-8") as file: 
            reader= csv.DictReader(file)
            values = set()
            for row in reader: 
                if row["Type 2"] != "": 
                    values.add(row["Type 2"])
            #ou values.discard("") a la place de la condition 

        Type2.objects.all().delete()
        for value in values : 
            Type2.objects.create(name=value, description="")

        for item in Type2.objects.all():
            print(f"Type 2 : {item.name}")

        
        # Step 3: Import Pokemons
        # Read values from the CSV file
        Pokemon.objects.all().delete()
        with open(PATH, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                pokemon = Pokemon(
                    name=row["Name"],
                    type1=Type1.objects.get(name=row["Type 1"]),
                    type2=Type2.objects.get(name=row["Type 2"]) if row["Type 2"]!= "" else None, 
                    hp= row["HP"], 
                    attack = row["Attack"], 
                    defense=row["Defense"], 
                    special_attack= row["Sp. Atk"], 
                    special_defense= row["Sp. Def"] , 
                    speed= row["Speed"], 
                    legendary=row["Legendary"] == "True", 
                    description= "" 
                )

                pokemon.save()

        for pokemon in Pokemon.objects.all():
            print(f"Pokemon : {pokemon.name}")