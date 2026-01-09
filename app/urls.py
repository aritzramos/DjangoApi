from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_lista_api, name='recipe_lista_api'),
]
