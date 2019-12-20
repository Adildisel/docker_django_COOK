from django.contrib import admin

from .models import Component, Recipe, Ingredient

admin.site.register(Ingredient)
admin.site.register(Component)
admin.site.register(Recipe)
