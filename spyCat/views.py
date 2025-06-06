from rest_framework import viewsets
from spyCat.models import SpyCat
from spyCat.serializers import SpyCatSerializer


class SpyCatViewSet(viewsets.ModelViewSet):
    queryset = SpyCat.objects.all()
    model = SpyCat
    serializer_class = SpyCatSerializer
