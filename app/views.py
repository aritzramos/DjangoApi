import requests
from django.shortcuts import render
from django.core import serializers


def recipe_lista_api(request):
    response = requests.get('http://127.0.0.1:8000/api/v1/recipes')
    
    recipe = response.json()
    return render(request, 'lista.html', {"recipe_mostrar":recipe})
