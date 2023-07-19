from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import permissions, status
from rest_framework.views import APIView
from .models import Drone, Order
from rest_framework import authentication
from api.serializers import DroneSerializer, LoadItemSerializer, OrderSerializer


class DronesAvailable(ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Drone.objects.filter(state__exact="IDL", battery_capacity__gt=25)
    serializer_class = DroneSerializer


class CreateDrone(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.SessionAuthentication]
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer


class DroneInformation(RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    lookup_field = 'serial_number'


class LoadingDrone(CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.SessionAuthentication]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CheckingItems(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, serial_number):
        order = Order.objects.filter(drone__serial_number__exact=serial_number,
                                     drone__state__exact='LDD').prefetch_related('load_items')
        items = order.load_items.all()
        serializer = LoadItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
