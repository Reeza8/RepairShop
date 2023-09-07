from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.db.models import Max

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

    def validate(self, data):
        devices = Device.objects.filter(customer=data['customer'], status=False)
        if devices:
            raise serializers.ValidationError("at least you have one device in accept queue")
        return data


class ProcessSerializer(serializers.ModelSerializer):
    lookup_field = 'tracking_code'
    def get_exit_date(self, obj):
        if obj.exit_date == None:
            return 'working on it'
        else:
            return obj.exit_date
    device = DeviceSerializer()
    exit_date = serializers.SerializerMethodField("get_exit_date")

    def validate(self, data):
        processes = Process.objects.filter(device=data['device']).aggregate(process_phase=Max("name"))
        # if device have any phases
        if processes['process_phase'] is not None:
            if data['name'] - processes['process_phase'] <= 0:
                raise serializers.ValidationError("device already has this phase")
            elif data['name'] - processes['process_phase'] > 1:
                raise serializers.ValidationError("you cant jump repair phases")
        # if start phase was not zero
        elif data['name'] != 0:
            raise serializers.ValidationError("process must start from zero phase")
        return data

    class Meta:
        model = Process
        fields = "__all__"


# input user data into the user token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        customer = Customer.objects.filter(user__username=user.username)
        if customer:
            token['type'] = "Customer"
        elif user.username == "admin":
            token['type'] = "admin"

        token['name'] = user.username
        token['first_name'] = user.first_name
        token['is_superuser'] = user.is_superuser
        return token


