from django.urls import path

from .views import *

urlpatterns = [
    path('recipes/list', list, name='recipe_list'),
    path('recipe/<int:index>', recipe, name='temporary_url')
]

app_name = "ledger"