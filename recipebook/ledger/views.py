from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import *
from .forms import *


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = 'ledger/add_image.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_pk'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        form.instance.recipe_pk = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ledger:recipe', kwargs={'pk': self.kwargs['pk']})
