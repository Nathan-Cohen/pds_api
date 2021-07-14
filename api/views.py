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
from rest_framework.generics import GenericAPIView


class pdsListe(GenericAPIView):
    serializer_class = pdsSerializers
    queryset = Pds.objects.all()
    # Affiche tous les PDS
    def get(self, request):
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
        #Vérifie que le mail est unique
        mailUnique = Pds.objects.filter(deleted=False, mail=pds1['mail'])
        if len(mailUnique) == 0:
            pds1_serializer = pdsSerializers(data=pds1)
            if pds1_serializer.is_valid():
                pds1_serializer.save()
                return JsonResponse(pds1_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(pds1_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return HttpResponse("Adresse mail déjà utilisé", status=status.HTTP_200_OK)



class details_pds(GenericAPIView):
    serializer_class = pdsSerializers
    # Affiche le PDS par ID
    def get(self, request, id):
        """
        Détail PDS
        """
        try:
            pds1 = Pds.objects.get(id=id)
        except Pds.DoesNotExist:
            return JsonResponse({'message': 'Ce PDS n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)

        #if request.method == 'GET':
        pds_serializer = pdsSerializers(pds1)
        return JsonResponse(pds_serializer.data, status=status.HTTP_200_OK)




    # Met à jour le PDS
    def patch(self, request, id):
        """
        Mise à jour PDS
        """
        # Recupère les données envoyés
        data = request.data
        # Récupère le pds a mettre à jour
        try:
            pds1 = Pds.objects.get(pk=id)
        except Pds.DoesNotExist:
            return JsonResponse({'message': 'Ce PDS n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)
        # Vérifie que le mail est unique et exclu le PDS en cours de modification
        mailUnique = Pds.objects.filter(deleted=False, mail=data['mail']).exclude(id=pds1.id)
        if len(mailUnique) == 0:
            # Met à jour les champs modifiés
            pds1.prenom = data.get("prenom", pds1.prenom)
            pds1.nom = data.get("nom", pds1.nom)
            pds1.mail = data.get("mail", pds1.mail)
            pds1.adresse = data.get("adresse", pds1.adresse)

            pds_serializer = pdsSerializers(pds1, data=data, partial=True)
            if pds_serializer.is_valid():
                pds_serializer.save()
                return JsonResponse(pds_serializer.data, status=status.HTTP_200_OK)
            return JsonResponse(pds_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return HttpResponse("Adresse mail déjà utilisé", status=status.HTTP_200_OK)

def base_pds(request):
    return render(request, 'pds_api/base_pds.html')
