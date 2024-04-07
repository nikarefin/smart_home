from rest_framework import serializers
from .models import *


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'timestamp']


class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(
        source='measurement_set',
        read_only=True,
        many=True
    )

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
