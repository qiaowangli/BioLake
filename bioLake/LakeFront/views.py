from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "LakeFront/index.html")

def test(request):
    print(request.POST.get('gene_name'))
    if request.POST.get('gene_name'):
        return render(request, "LakeFront/test.html", {'gene':request.POST.get('gene_name')})
    else:
        render(request, "LakeFront/index.html")

