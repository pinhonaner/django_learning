from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home/pages/home.html')

def recipe(request, recipe_id):
    return render(request, 'home/pages/recipe-view.html')


