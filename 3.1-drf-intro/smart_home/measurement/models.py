from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'Датчик {self.name}'


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor, on_delete=models.CASCADE, related_name='sensor_measurement')
    temperature = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
