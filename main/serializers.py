from rest_framework import serializers
from .models import PollutionReport, CleanupEvent, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'town')

class PollutionReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollutionReport
        fields = ('id', 'pollution_types', 'location', 'created_at', 'updated_at', 'user', 'size')

class CleanupEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleanupEvent
        fields = ('id', 'participants', 'report', 'scheduled_for', 'meeting_point', 'description')