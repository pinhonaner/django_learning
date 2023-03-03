from django.urls import path

from home import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),  # tested
    path('recipe/<int:id>/', views.recipe, name="recipe"),  # tested
    path('recipe/category/<int:category_id>/',
         views.category, name="category")  # tested
]
