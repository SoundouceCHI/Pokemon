from django.urls import path
from monsters.views import view_pokemon, create_pokemon, edit_pokemon

app_name = "monsters"

urlpatterns = [
    path("view/<uuid:uuid>", view_pokemon, name="view_pokemon"), 
    path("create", create_pokemon, name="create_pokemon"), 
    path("edit/<uuid:uuid>", edit_pokemon, name="edit_pokemon")
]