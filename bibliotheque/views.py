from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bibliotheque(request):
    return render(request,'bibliotheque/liste_documents.html')