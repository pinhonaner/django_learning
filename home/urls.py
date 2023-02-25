from django.urls import path
from home import views

urlpatterns = [
    path('', views.home), # www.dominio.com/
    path('recipe/<int:recipe_id>/', views.recipe)
]
