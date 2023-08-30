from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from rest_framework import generics
from django.shortcuts import get_object_or_404

class CustomerViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Customer.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(user)
        return Response(serializer.data)


class DeviceViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Device.objects.all()
        print(queryset)
        serializer = DeviceSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Device.objects.all()
        device = get_object_or_404(queryset, pk=pk)
        serializer = DeviceSerializer(device)
        return Response(serializer.data)


class ProcessViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Process.objects.all()
        print(queryset)
        serializer = ProcessSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Process.objects.all()
        process = get_object_or_404(queryset, pk=pk)
        serializer = ProcessSerializer(process)
        return Response(serializer.data)