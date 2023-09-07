from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from django.shortcuts import get_object_or_404
import uuid
import jwt
from RepairShop.settings import SECRET_KEY
from .models import *
from django.db.models import Q
import datetime


# Check the access of user from token claims
def permissions(request, userwithaccess):
    token_str = str(request.auth)
    token_byte = bytes(token_str, 'utf-8')
    dic = jwt.decode(token_byte, SECRET_KEY, algorithms=["HS256"])
    return dic['type'] == userwithaccess


def get_device_filter(request):
    device_query = Q()
    if 'device_name' in request.GET:
        device_query &= Q(name=request.GET["device_name"])
    if 'problem' in request.GET:
        device_query &= Q(problem=request.GET["problem"])
    if 'status' in request.GET:
        device_query &= Q(status=request.GET["status"])
    if 'customer' in request.GET:
        device_query &= Q(customer__user__username=request.GET["customer"])
    if 'tracking_code' in request.GET:
        device_query &= Q(tracking_code=request.GET["tracking_code"])
    return device_query


def get_process_filter(request):
    process_query = Q()
    if 'id' in request.GET:
        process_query &= Q(id=request.GET["id"])
    if 'name' in request.GET:
        process_query &= Q(name=request.GET["name"])
    if 'entry_date' in request.GET:
        process_query &= Q(entry_date=request.GET["entry_date"])
    if 'exit_date' in request.GET:
        process_query &= Q(exit_date=request.GET["exit_date"])
    return process_query


class CustomerViewSet(viewsets.ViewSet):
    def list(self, request):
        if not permissions(request, 'admin'):
            return Response({"access denied"}, status=403)
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        if not permissions(request, 'admin'):
            return Response({"access denied"}, status=403)
        queryset = Customer.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(user)
        return Response(serializer.data)


class DeviceViewSet(viewsets.ViewSet):
    lookup_field = 'tracking_code'

    def list(self, request):
        if permissions(request, 'Customer'):
            customer = Customer.objects.get(user_id=request.user.id)
            queryset = Device.objects.filter(customer=customer.id)
        else:
            queryset = Device.objects.filter(get_device_filter(request))
        serializer = DeviceSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, tracking_code):

        queryset = Device.objects.all()
        device = get_object_or_404(queryset, tracking_code=tracking_code)
        serializer = DeviceSerializer(device)
        return Response(serializer.data)

    def create(self, request):
        if 'status' in request.data or 'factor' in request.data\
                    or 'tracking_code' in request.data:
            if not permissions(request, 'admin'):
                return Response({"Error": "only admin could set status,factor and tracking_code"}, status=403)

        new_data = request.data.copy()
        if 'customer' not in request.data:
            customer = Customer.objects.get(user_id=request.user.id)
            new_data['customer'] = customer.id

        # produce tracking code
        t_code = uuid.uuid4().hex[:10].upper()

        new_data['tracking_code'] = t_code
        serializer = DeviceSerializer(data=new_data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        serializer.save()
        return Response({"کد رهگیری": t_code})


class ProcessViewSet(viewsets.ViewSet):
    def list(self, request):
        if permissions(request, 'admin'):
            devices = Device.objects.filter(get_device_filter(request))
            main_query = Process.objects.none()
            for device in devices:
                query = Process.objects.filter(get_process_filter(request), device=device)
                main_query = main_query.union(query)
            queryset = main_query
        else:
            customer = Customer.objects.get(user_id=request.user.id)
            devices = Device.objects.filter(customer__id=customer.id)
            process_query = Process.objects.none()
            for device in devices:
                processes = Process.objects.filter(device=device)
                process_query = process_query.union(processes)
            queryset = process_query
        serializer = ProcessSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Process.objects.all()
        process = get_object_or_404(queryset, pk=pk)
        serializer = ProcessSerializer(process)
        return Response(serializer.data)

    def create(self, request):
        if not permissions(request, 'admin'):
            return Response({"Error": "you need admin access"}, status=403)

        serializer = ProcessSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        process = Process.objects.filter(name=int(request.data['name'])-1, device=request.data["device"]).first()

        if process:
            process.exit_date = datetime.date.today()
            process.save()

        serializer.save()
        return Response(serializer.data)


