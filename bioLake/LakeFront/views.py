from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "LakeFront/index.html")

def test(request):
    return render(request, "LakeFront/test.html", {'gene':request.POST.get('gene_name')})

def geneAnalysis(request):
    if(len(request.POST.keys()) != 0):
        return render(request, "mRNAStage/index.html", {'analysisType':request.POST.get('analysisType'), 'geneData': request.POST.get('geneData'),'geneID': request.POST.get('geneID')})
    else:
        return render(request, "mRNAStage/index.html", {'analysisType':request.GET.get('analysisType'), 'geneData': request.GET.get('geneData'),'geneID': request.GET.get('geneID')})


