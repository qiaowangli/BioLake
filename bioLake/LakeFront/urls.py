from django.urls import path
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('geneAnalysis/', views.test),
    path('mRNA/', include('mRNAStage.urls')),
    path('DNA/', include('DNAStage.urls')),
    path('mixture/', include('mixtureStage.urls')),
    path('ML/', include('MlStage.urls'))
]
