from rest_framework import serializers
from . models import jadwalModels

class jadwalserializer(serializers.ModelSerializer):
    class Meta:
        model = jadwalModels
        fields = "__all__"