from django.db import models


class Pds(models.Model):
    firstname = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.firstname