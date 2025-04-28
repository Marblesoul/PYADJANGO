from rest_framework import serializers
from measurement.models import Sensor, Measurement

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'sensor', 'temperature', 'created_at', 'image']

class MeasurementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
