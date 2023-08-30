from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=150)


class Device(models.Model):
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    factor = models.TextField()
    problem = models.CharField(max_length=100)
    point = models.IntegerField(default=0)


class Process(models.Model):
    name = models.CharField(max_length=100)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    description = models.TextField()
    entry_date = models.DateField(auto_now_add=True)
    exit_date = models.DateField()
