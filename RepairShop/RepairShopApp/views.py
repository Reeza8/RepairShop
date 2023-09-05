from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from rest_framework import generics
from django.shortcuts import get_object_or_404
import uuid
import jwt
from RepairShop.settings import SECRET_KEY

# Check the access of user from token claims


def permissions(request, userwithaccess):
    token_str = str(request.auth)
    token_byte = bytes(token_str, 'utf-8')
    dic = jwt.decode(token_byte, SECRET_KEY, algorithms=["HS256"])

    if dic['type'] is not userwithaccess:
        raise Exception(f"{userwithaccess} have access to this data")
    else:
        return True




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
    #dastresi bede ke faghat admin biad inja
    def list(self, request):
        queryset = Device.objects.all()
        serializer = DeviceSerializer(queryset, many=True)
        return Response(serializer.data)

    #dastresi bede ke faghat admin biad inja
    def retrieve(self, request, pk=None):
        queryset = Device.objects.all()
        device = get_object_or_404(queryset, pk=pk)
        serializer = DeviceSerializer(device)
        return Response(serializer.data)

    def create(self, request):
        if 'status' in request.data or 'factor' in request.data\
                    or 'tracking_code' in request.data:
            if not permissions(request, 'admin'):
                raise Exception("only admin could set status,factor and tracking_code")

        new_data = request.data.copy()
        if 'customer' not in request.data:
            customer = Customer.objects.get(user_id=request.user.id)
            new_data = request.data.copy()
            new_data['customer'] = customer.id

        # produce tracking code
        t_code = uuid.uuid4().hex[:6].upper()

        new_data['tracking_code'] = t_code
        serializer = DeviceSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            dict_response = {"کد رهگیری": t_code}
        else:
            dict_response = {"message": "Error During Saving Data"}

        return Response(dict_response)


class ProcessViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Process.objects.all()
        serializer = ProcessSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Process.objects.all()
        process = get_object_or_404(queryset, pk=pk)
        serializer = ProcessSerializer(process)
        return Response(serializer.data)