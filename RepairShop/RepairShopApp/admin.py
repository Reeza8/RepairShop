from django.contrib import admin
from .models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'address', 'phone_number' )
    empty_value_display = '-empty-'


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'customer', 'tracking_code', 'status')
    search_fields = ['customer']
    empty_value_display = '-empty-'


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'device', 'entry_date')
    search_fields = ['entry_date']
    empty_value_display = '-empty-'

