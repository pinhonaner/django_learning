from django.urls import path
from home import views

urlpatterns = [
    path('', views.home), # www.dominio.com/
    path('sobre/', views.sobre), # www.dominio.com/sobre/
    path('contato/', views.contato), # www.dominio.com/contato/
]
