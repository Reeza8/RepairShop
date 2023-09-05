from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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


