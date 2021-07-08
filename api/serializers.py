from rest_framework import serializers
from .models import Pds

class pdsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Pds
        fields = "__all__"