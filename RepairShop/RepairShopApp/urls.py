from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.SimpleRouter()
router.register("customers", CustomerViewSet, basename='customers')
router.register("devices", DeviceViewSet, basename='devices')
router.register("process", ProcessViewSet, basename='process')

urlpatterns = [
    path('', include(router.urls)),


]
