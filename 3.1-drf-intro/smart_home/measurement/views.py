from rest_framework.response import Response
from rest_framework.decorators import api_view
from measurement.models import Sensor
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


@api_view(['GET', 'POST', 'PATCH'])
def sensors(request, pk=None):
    if request.method == 'GET':
        if pk:
            sensor = Sensor.objects.get(pk=pk)
            ser = SensorDetailSerializer(sensor)
            return Response(ser.data)
        all_sensors = Sensor.objects.all()
        ser = SensorSerializer(all_sensors, many=True)
        return Response(ser.data)
    if request.method == 'POST':
        ser = SensorSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)
    if request.method == 'PATCH':
        sensor = Sensor.objects.get(pk=pk)
        ser = SensorSerializer(sensor, data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)

@api_view(['POST'])
def measurements(request):
    if request.method == 'POST':
        ser = MeasurementSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)