from rest_framework.viewsets import ModelViewSet
from sensors.serializers import *


class SensorsViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementsViewSet(ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
