from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import *


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/list.html'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/recipe.html'
