from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def membres(request):
    return HttpResponse(' Gère linscription et les interactions des membres avec la bibliothèque.')