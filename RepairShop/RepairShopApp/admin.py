from django.contrib import admin
from .models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address','phone_number' )
    search_fields = ['name']
    list_filter = ('name',)
    empty_value_display = '-empty-'


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer', 'problem')
    search_fields = ['customer']
    empty_value_display = '-empty-'


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('name', 'device', 'entry_date')
    search_fields = ['entry_date']
    empty_value_display = '-empty-'

# name = model
# device = mod
# description
# entry_date =
# exit_date =