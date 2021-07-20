from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('base_pds/api', views.pdsListe, basename='pdsListe')
router.register('fiche_profil', views.details_pds, basename='details_pds')
router.register('base_pds/pds', views.base_pds, basename='base_pds')
router.register('base_pds/pds/id', views.details_pds, basename='base_pds')

