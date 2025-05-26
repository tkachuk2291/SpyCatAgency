from rest_framework import viewsets
from spyCat.models import SpyCat, Breed
from spyCat.serializers import SpyCatSerializer, BreedSerializer


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    model = Breed
    serializer_class = BreedSerializer


class SpyCatViewSet(viewsets.ModelViewSet):
    queryset = SpyCat.objects.all()
    model = SpyCat
    serializer_class = SpyCatSerializer
