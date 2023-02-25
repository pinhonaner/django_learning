from django.shortcuts import render
from utils.recipes.factory import make_recipe

# Create your views here.

def home(request):
    return render(request, 'home/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })

def recipe(request, recipe_id):
    return render(request, 'home/pages/recipe-view.html', context={
        'recipe': make_recipe(),
    })


