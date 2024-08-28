
from rest_framework import serializers
from datetime import datetime

class PublicHolidaySerializer(serializers.Serializer):
    date = serializers.DateField()
    localName = serializers.CharField()
    name = serializers.CharField()
    countryCode = serializers.CharField()
    fixed = serializers.BooleanField()
    globalHoliday = serializers.BooleanField(source='global', allow_null=True, required=False)
    counties = serializers.CharField(allow_null=True, required=False)
    launchYear = serializers.IntegerField(allow_null=True, required=False)
    typeHoliday = serializers.CharField(source='type', allow_null=True, required=False)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        date = representation.get('date')

        if date:
            date_object = datetime.strptime(date, '%Y-%m-%d').date()
            day_of_week = date_object.strftime('%A')
            representation['dayOfWeek'] = day_of_week

        else:
            representation['dayOfWeek'] = 'Unknown'

        return representation
