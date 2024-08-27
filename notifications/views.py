from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def notification_view(request):
    return  HttpResponse('Gère les rappels et les alertes pour les emprunts et retours.')