import requests
from rest_framework import serializers
from spyCat.models import SpyCat, Breed


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('id', 'name')

    def validate_name(self, value):
        response = requests.get('https://api.thecatapi.com/v1/breeds')
        if response.status_code != 200:
            raise serializers.ValidationError("Failed to validate breed: TheCatAPI unavailable")

        breeds = response.json()
        valid_breeds = [breed['name'].lower() for breed in breeds]

        if value.lower() not in valid_breeds:
            raise serializers.ValidationError(f"Breed '{value}' is not recognized by TheCatAPI.")

        return value


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ('id', 'name', "years_of_experience", "breed", "salary")

