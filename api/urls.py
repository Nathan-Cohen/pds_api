from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('base_pds/api/', views.pdsListe.as_view()),
    path('fiche_profil/<int:id>/', views.details_pds.as_view()),
    path('base_pds/pds/', views.base_pds)
]

