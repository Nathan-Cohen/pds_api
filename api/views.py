from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Pds
from .serializers import pdsSerializers


class pdsListe(APIView):
    # Affiche tous les PDS
    def get(self, request):
        # sélectionne tous les PDS qui ne sont pas marqués comme supprimer
        pds1 = Pds.objects.filter(supprimer=False)
        pds1_serializer = pdsSerializers(pds1, many=True)
        return Response(pds1_serializer.data)

    # Créer un nouveau PDS
    def post(self, request):
        pds1 = JSONParser().parse(request)
        pds1_serializer = pdsSerializers(data=pds1)
        if pds1_serializer.is_valid():
            pds1_serializer.save()
            return JsonResponse(pds1_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(pds1_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class details_pds(APIView):
    # Affiche le PDS par ID
    def get(self, request, id):
        try:
            pds1 = Pds.objects.get(pk=id)
        except Pds.DoesNotExist:
            return JsonResponse({'message': 'Ce PDS n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)

        #if request.method == 'GET':
        pds_serializer = pdsSerializers(pds1)
        return JsonResponse(pds_serializer.data, status=status.HTTP_201_CREATED)




    # Met à jour le PDS
    def update(self, request, id):
        # Recupère les données envoyés
        data = request.DATA

        try:
            pds1 = Pds.objects.get(pk=id)
        except Pds.DoesNotExist:
            return JsonResponse({'message': 'Ce PDS n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)

        pds_serializer = pdsSerializers(pds1, data=data, many=True, partial=True)
        if pds_serializer.is_valid():
            pds_serializer.save()
            return JsonResponse(pds_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(pds_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

