from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bibliotheque(request):
    return HttpResponse('  Gère la classification des documents, ainsi que la gestion des livres et revues.')