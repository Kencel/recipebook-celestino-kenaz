from django.contrib import admin
from .models import *


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInLine]


class IngredientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
