from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def comptabilite(request):
    return HttpResponse("<h1>Gère les paiements et les amendes</h1>")