from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def firstPageView(request):
    return HttpResponse('Notre page d\'accueil')