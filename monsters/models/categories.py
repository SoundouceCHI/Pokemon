from django.db import models

class Type1(models.Model): 
    name= models.CharField(max_length=64, blank=False, unique=True, verbose_name="name")
    description = models.TextField(verbose_name="description", blank=True)
    
    class Meta:
        verbose_name = "element"
        verbose_name_plural = "elements"

    def __str__(self):
        return f"{self.name}"


class Type2(models.Model):
    """Effect type for a Pokémon."""
    name = models.CharField(max_length=64, blank=False, unique=True, verbose_name="name")
    description = models.TextField(blank=True, verbose_name="description")

    class Meta:
        verbose_name = "effect"
        verbose_name_plural = "effects"

    def __str__(self):
        return f"{self.name}"