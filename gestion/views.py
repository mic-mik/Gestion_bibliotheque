from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def gestion_bibliotheque(request):
    return HttpResponse('Gère les rapports et les statistiques de la bibliothèque.')