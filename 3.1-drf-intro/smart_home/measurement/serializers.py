from rest_framework import serializers

from .models import Measurement, Sensor


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at', 'updated_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(
        read_only=True, many=True, source="sensor_measurement")

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
