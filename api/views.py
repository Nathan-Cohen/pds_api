from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Pds
from .serializers import pdsSerializers
from rest_framework import viewsets


class pdsListe(viewsets.ViewSet):
    #serializer_class = pdsSerializers
    #queryset = Pds.objects.all()
    # Affiche tous les PDS
    def list(self, request):
        """
        Liste PDS
        """
        # sélectionne tous les PDS qui ne sont pas marqués comme supprimer
        pds1 = Pds.objects.filter(deleted=False)
        pds1_serializer = pdsSerializers(pds1, many=True)
        return Response(pds1_serializer.data)

    # Créer un nouveau PDS
    def post(self, request):
        """
        Nouveau PDS
        """
        pds1 = JSONParser().parse(request)
        pds1_serializer = pdsSerializers(data=pds1)
        if pds1_serializer.is_valid():
            pds1_serializer.save()
            return JsonResponse(pds1_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(pds1_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class details_pds(viewsets.ViewSet):
    # Affiche le PDS par ID
    def get(self, request, pk):
        """
        Détail PDS
        """
        try:
            pds1 = Pds.objects.get(pk=pk)
        except Pds.DoesNotExist:
            return JsonResponse({'message': 'Ce PDS n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)

        pds_serializer = pdsSerializers(pds1)
        return JsonResponse(pds_serializer.data, status=status.HTTP_200_OK)

    # Met à jour le PDS
    def partial_update(self, request, pk):
        """
        Mise à jour PDS
        """
        # Recupère les données envoyés
        data = request.data
        # Récupère le pds a mettre à jour
        try:
            pds1 = Pds.objects.get(pk=pk)
        except Pds.DoesNotExist:
            return JsonResponse({'message': 'Ce PDS n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)

        # Met à jour les champs modifiés
        pds_serializer = pdsSerializers(pds1, data=data, partial=True)
        if pds_serializer.is_valid():
            pds_serializer.save()
            return JsonResponse(pds_serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(pds_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Recupère les données envoyés
        data = request.data

        try:
            pds1 = Pds.objects.get(pk=pk)
        except Pds.DoesNotExist:
            return JsonResponse({'message': 'Ce PDS n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)

        # Met à jour les champs modifiés
        pds_serializer = pdsSerializers(pds1, data=data, partial=True)
        if pds_serializer.is_valid():
            pds_serializer.save()
            return JsonResponse({'message':'PDS supprimé'}, status=status.HTTP_200_OK)
        return JsonResponse(pds_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class base_pds(viewsets.ViewSet):
    def list(self, request):
        return render(request, 'pds_api/base_pds.html')
