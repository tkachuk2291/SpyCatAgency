from rest_framework import viewsets, status
from rest_framework.response import Response

from Mission.models import Mission, Target
from Mission.serializers import MissionSerializer, TargetSerializer


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    model = Mission
    serializer_class = MissionSerializer

    def destroy(self, request, *args, **kwargs):
        mission = self.get_object()
        if mission.cat is not None:
            return Response(
                {"error": "Mission assigned to a cat cannot be deleted."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)

class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    model = Target
    serializer_class = TargetSerializer
