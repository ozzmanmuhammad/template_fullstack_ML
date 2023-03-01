from .models import animalIdentifier
from rest_framework import serializers

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = animalIdentifier
        fields = '__all__'
