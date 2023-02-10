from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Welcome to the BioLake power by UCalgary")
    return render(request, "LakeFront/index.html")

