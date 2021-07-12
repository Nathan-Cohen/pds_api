from django.db import models


class Pds(models.Model):
    id = models.AutoField(primary_key=True)
    prenom = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    mail = models.EmailField(max_length=100)
    adresse = models.CharField(max_length=100)
    supprimer = models.CharField(max_length=100, default='False')

    def __str__(self):
        return self.prenom