# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response


class SensorCreateListView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreateView(CreateAPIView):
    serializer_class = MeasurementSerializer
