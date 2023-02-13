from django.urls import path
from django.urls import path, include
from django.urls import re_path

from . import views

urlpatterns = [
    path('', views.index),
    path('geneAnalysis/', views.test),
    re_path(r'^pipeline/$', views.geneAnalysis),
    path('pipeline/', views.geneAnalysis),
    path('pipeline/current.html', include('mRNAStage.urls'))
    # path('DNA/', include('DNAStage.urls')),
    # path('mixture/', include('mixtureStage.urls')),
    # path('ML/', include('MlStage.urls'))
]
