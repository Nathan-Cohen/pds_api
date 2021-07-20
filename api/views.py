from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse
from .models import Pds
from .serializers import pdsSerializers
from rest_framework import viewsets


class pdsListe(viewsets.ViewSet):
    # Affiche tous les PDS
    def list(self, request):
        # sélectionne tous les PDS qui ne sont pas marqués comme supprimer
        queryset = Pds.objects.filter(deleted=False)
        list_pds_serializer = pdsSerializers(queryset, many=True)
        return Response(list_pds_serializer.data)

    # Créer un nouveau PDS
    def post(self, request):
        new_pds_serializer = pdsSerializers(data=request.data)
        if new_pds_serializer.is_valid():
            new_pds_serializer.save()
            return JsonResponse(new_pds_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(new_pds_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class details_pds(viewsets.ViewSet):
    # Affiche le detail d'un PDS par ID
    def get(self, request, pk):
        queryset = Pds.objects.filter(pk=pk)
        list_pds_serializer = pdsSerializers(queryset, many=True)
        return Response(list_pds_serializer.data, status=status.HTTP_200_OK)

    # Met à jour le PDS
    def partial_update(self, request, pk):
        queryset = Pds.objects.get(pk=pk)
        # Recupère les données envoyés
        new_pds_serializer = pdsSerializers(queryset, data=request.data, partial=True)
        if new_pds_serializer.is_valid():
            new_pds_serializer.save()
            return Response(new_pds_serializer.data, status=status.HTTP_200_OK)
        return Response(new_pds_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
