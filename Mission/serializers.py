from rest_framework import serializers
from Mission.models import Mission, Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ('id', 'name', 'mission', 'country', 'notes', 'complete_state')

    def validate(self, data):
        target = self.instance
        mission = None
        if target:
            mission = target.mission
        else:
            mission = self.context.get('mission')

        if target and data.get('notes') and (target.complete_state or (mission and mission.complete_state)):
            raise serializers.ValidationError("Cannot update notes if the target or mission is completed.")

        return data

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ('id', 'cat', "complete_state")
